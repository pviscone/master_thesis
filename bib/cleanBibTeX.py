#! /usr/bin/env python3
# Author: Izaak Neutelings (July 2022)
# Description:
#   Clean BibTeX file: key ordering, capitalization, indentation, spacing, ...
#   and detect potential issues.
# Note:
#   * If you use the same input/output name, use --backup to create a backup file of the original !
#   * Following CMS guidelines:
#     https://twiki.cern.ch/twiki/bin/viewauth/CMS/Internal/PubGuidelines#References
#     https://gitlab.cern.ch/tdr/utils/-/blob/master/general/cleanRefs.py
# Instructions:
#   curl https://raw.githubusercontent.com/IzaakWN/CodeSnippets/master/LaTeX/cleanBibTeX.py > cleanBibTeX.py
#   ./cleanBibTeX.py thesis.bib
#   ./cleanBibTeX.py thesis.bib -o thesis.bib --backup
#   ./cleanBibTeX.py thesis.bib --check -o thesis_clean.bib  # do checks
#   ./cleanBibTeX.py thesis.bib > thesis_clean.bib           # careful of picking up warnings
from __future__ import print_function
import os, re, stat
from math import ceil
import textwrap
from collections import OrderedDict
rexp_tag = re.compile(r'^\s*@(\w+)\s*{(.*)') # @type{label,
rexp_key = re.compile(r'^\s*([\w-]+)\s*=\s*(.*)')
rexp_let = re.compile(r'[a-zA-Z]') # any alphabetic letter
rexp_acc = re.compile(r'(?<!{)\\["`\'~=cuvhao]',re.IGNORECASE) # unprotected accent
rexp_vol_JHEP = re.compile(r'^[0-9]{2}$') # JHEP volume must be exactly two numbers (0 left padded)
key_dict = {k.lower(): k for k in ['archivePrefix','primaryClass','reportNumber','SLACcitation']} # enforce capitalization
keys_top = [ # order for items on top of BibTeX entry
  'author','title','editor',
  'collaboration','institution','address',
]
keys_bottom = [ # order for items on bottom of BibTeX entry
  'journal','volume','number','year','pages','doi',
  'reportNumber','series','publisher','howpublished','url','note',
  'eprint','archivePrefix','primaryClass','SLACcitation',
]
space_entr = 1   # number of white lines between entries
space_max  = 2   # maximum number of white lines any item
line_max   = 110 # rough maximum number of characters per item line
warnings   = { }
duplicates = { # look for duplicate DOIs, eprints
  'doi': { },
  'eprint': { }
}
journals   = { # misspelled journals
  'J. Instrum.':          'JINST',
  'J. High Energy Phys.': 'JHEP',
}
#journals = {k.lower().replace('.',''): v for k, v in journals.items()}


def write(outfile,line):
  """Help function to print/write line."""
  if outfile:
    outfile.write(line+'\n')
  print(line)
  

def ensuredir(dname,verb=0):
  """Make directory if it does not exist."""
  if not os.path.exists(dname):
    if verb>=1:
      print(f">>> Making directory {dname}...")
    os.makedirs(dname)
  return dname
  

def warning(string,**kwargs):
  print(f">>> \033[1m\033[93m{kwargs.get('pre','')}Warning!\033[0m\033[93m {string}\033[0m")
  

def splititem(fullstr,nmax=line_max):
  """Split long line of field value at spaces."""
  assert '\n' not in fullstr
  if fullstr.count(' ')<=3: # don't bother
    return [fullstr]
  nrows = ceil(len(fullstr)/float(nmax)) # aim for this number of rows
  nmax  = max(len(fullstr)/float(nrows),max(len(s) for s in fullstr.split())+1)
  wrapstr = textwrap.fill(fullstr,width=nmax,break_on_hyphens=False)
  while wrapstr.count('\n')+1>nrows:
    ###nrows_ = wrapstr.count('\n')+1
    ###print(f">>> splititem: Rows={nrows_} vs. target {nrows}. Try wraping again with nmax = {nmax} -> {nmax+3}")
    nmax += 3 # increase maximum number of characters per line
    wrapstr = textwrap.fill(fullstr,width=nmax,break_on_hyphens=False)
  lines = wrapstr.split('\n')
  return lines
  

def sortkey(key):
  """Sort field keys from global keys_top and keys_bottom lists."""
  ikey = len(keys_top)+1
  if isinstance(key,tuple):
    key = key[0]
  if key in keys_top:
    ikey = keys_top.index(key)
  elif key in keys_bottom:
    ikey = ikey+2+keys_bottom.index(key) 
  return ikey
  

def writeComparisonFiles(infname,outfname,labels,compile=False,cmstdr=False):
  """Create TeX document to compare PDF output in order to validate reformatted BibTeX file."""
  import shutil
  import subprocess
  from datetime import datetime
  outdir = os.path.join(os.path.dirname(outfname),"cleanBibTexTest")
  olddir = ensuredir(os.path.join(outdir,"old")) # compile in subdirectories
  newdir = ensuredir(os.path.join(outdir,"new")) # compile in subdirectories
  oldtexfname = os.path.join(olddir,os.path.basename(infname[:-4]+'.tex'))
  newtexfname = os.path.join(newdir,os.path.basename(outfname[:-4]+'.tex'))
  texfnames = [ ]
  for subdir, bibfname in [('old',infname),('new',outfname)]:
    texdir   = ensuredir(os.path.join(outdir,f"{subdir}/"))
    texfname = os.path.basename(infname[:-4]+'.tex') # use original name to compile
    texfnames.append((texdir,texfname))
    texfname = os.path.join(texdir,texfname)
    bibpath  = os.path.join(texdir,os.path.basename(infname)) # full path
    shutil.copyfile(bibfname,bibpath)
    print(f">>> Writing citations to {texfname} for comparison...")
    with open(texfname,'w') as texfile:
      texfile.write(f"% Auto-generated by cleanBibTeX.py on {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}\n")
      texfile.write(f"% for comparing compiled PDFs via https://www.diffchecker.com/pdf-diff/\n")
      if cmstdr:
        maxchars = 68
        texfile.write('\n')
        texfile.write(r'{\small'+'\n')
      else:
        maxchars = 80
        texfile.write(r"\documentclass[11pt]{article}"+'\n')
        texfile.write(r"\usepackage[margin=2cm]{geometry}"+'\n')
        texfile.write(r"\usepackage{amsmath,hyperref}"+'\n')
        texfile.write(r"\usepackage[hyperref=true,natbib=true,backend=bibtex,style=numeric,sorting=none]{biblatex}"+'\n')
        texfile.write(r"\newcommand*{\DOI}[1]{\textsc{doi:}~\href{http://dx.doi.org/#1}{\texttt{#1}}}"+"\n")
        #texfile.write(fr"\bibliography{{{os.path.basename(bibpath)}}}"+"\n")
        texfile.write(fr"\addbibresource{{{os.path.basename(bibpath)}}}"+"\n")
        texfile.write(r"\begin{document}"+"\n\n")
      texfile.write(fr"Citing from\\"+'\n')
      texfile.write(fr"\verb|{bibpath}|:\\"+'\n')
      nchars = 0
      ###labels = labels[:50] # for debugging
      for i, label in enumerate(labels,1):
        line = fr"\verb|{label}|~\cite{{{label}}}"
        nchars += len(label)+3
        if i==len(labels): # last citation
          line += r".\\"+"\n\n"
        elif nchars<maxchars:
          line += ", "
        else: # wrap/break line
          line = r"\\"+'\n'+line+r", "
          nchars = len(label)+3
        texfile.write(line)
      if cmstdr:
        texfile.write(r'}'+'\n')
        texfile.write(r"\bibliography{auto_generated}"+"\n\n")
      else:
        texfile.write(r"\printbibliography"+"\n\n")
        texfile.write(r"\end{document}"+'\n')
  cmds = [ ]
  scripts = [ ]
  for texdir, texfname in texfnames:
    sname = os.path.join(texdir,texfname.replace('.tex','.sh'))
    scripts.append(sname)
    with open(sname,'w') as script:
      cmds_ = [ f"cd {texdir}" ]
      script.write('#! /bin/bash')
      script.write(f"# Auto-generated by cleanBibTeX.py on {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}\n")
      script.write('function peval { echo -e ">>> $@"; eval "$@"; }\n')
      if cmstdr:
        style = 'paper' if '/papers/' in texfname else 'an' if '/notes/AN-' in texfname else 'pas' #tdr/note/an/pas/cr/in/paper
        cmds_.append(f"../../utils/tdr --preview --style={style} --noclean --temp_dir=. b {texfname}")
      else:
        auxfname = texfname[:-4]+'.aux'
        pdffname = texfname[:-4]+'.pdf'
        pdfcmd   = f"pdflatex -interaction=nonstopmode {texfname}"
        cmds_.append(f"{pdfcmd} && bibtex {auxfname} && {pdfcmd} && {pdfcmd} && open {pdffname}")
      for cmd in cmds_:
        script.write(f'peval "{cmd}"\n')
        cmds.append(cmd)
    os.chmod(sname,stat.S_IRWXU)
  if compile:
    for script in scripts:
      printsep()
      print(f">>>\n>>> Executing script {script}...")
      os.system(script)
      #process = subprocess.Popen(subcmd,stdout=subprocess.PIPE,shell=True)
      #print(process.communicate())
    printsep()
    print(f">>> Please find comparison output in {outdir}")
  else:
    print(">>> Compile with:")
    for cmd in cmds:
      print(f">>>   {cmd}")
  print(">>> Compare PDFs on https://www.diffchecker.com/pdf-diff/ or with Adobe Acrobat")
  

def printsep(w=120,n=2,c='#',wl=True):
  """Print seperator."""
  if wl: print()
  for i in range(n): print(c*w)
  if wl: print()
  

class Entry:
  """Container class for BibTeX entry."""
  
  def __init__(self,btype,label):
    self.type       = btype.lower().replace('phd','PhD')
    self.label_full = label.strip() # including stuff after comma
    self.label      = self.label_full.split(',')[0] # up until comma
    self.fields     = OrderedDict()
    self.firstline  = f"@{self.type}{{{self.label_full}"
    self.lastline   = ""
    label_          = self.label_full.split('%')[0] # ignore comments
    assert ',' in label_, f"Found no comma in label... Expect '@type{{label,' format, got '{tagline}'..."
    assert '=' not in label_, f"Found equal sign in label... Expect '@type{{label,' format, got '{tagline}'..."
  
  @classmethod
  def fromfile(cls,tagline,infile,verb=0):
    """Construct Entry object from lines of given input file."""
    match  = rexp_tag.search(tagline) # parse '@type{label,'
    entry  = cls(match.group(1),match.group(2)) # container object
    items  = { }
    key    = None
    nleft  = tagline.count('{')-tagline.count('\{')
    nright = tagline.count('}')-tagline.count('\}')
    for line in infile: # find entire BibTeX entry from next lines
      nleft += line.count('{')-line.count('\{')
      nright += line.count('}')-line.count('\}')
      if nleft==nright: # brace closing '@type{{label,' of this BibTex entry
        entry.lastline = line.strip()
        break
      assert not rexp_tag.search(line), f"Found '@type{{label,' in BibTeX entry '{line}'. Brace of previous entry not closed?"
      match = rexp_key.search(line) # find new item key
      if match:
        key = match.group(1).strip().lower()
        key = key_dict.get(key,key) # format capitalization of keys
        entry.fields[key] = match.group(2)
      elif key!=None: # add to previous item
        entry.fields[key] += ' '+line.strip()
    assert entry.lastline, f"Did not find last line for {entry.label}"
    #print(next(infile))
    return entry
  
  def sortkeys(self):
    """Sort fields by given order."""
    self.fields = OrderedDict(sorted(self.fields.items(),key=lambda k: sortkey(k[0])))
    return list(self.fields.keys())
  
  def checkfields(self):
    """Check fields, and prepare warnings."""
    for key in self.fields.keys():
      lkey   = key.lower()
      value  = self.fields[key].strip('"{}, ')
      lvalue = value.lower()
      if lkey in ['author','school','publisher','journal']:
        matches = rexp_acc.findall(lvalue) # look for unprotected characters
        if matches:
          warnings.setdefault(r'Found unprotected special character (e.g. \"o -> {\"o}):',[ ]).append((self.label,f"{key} = {self.fields[key]}"))
      if self.type=='article' and 'page' in lkey and '-' in value:
        warnings.setdefault("CMS format of 'pages' cannot contain range:",[ ]).append((self.label,f"{key} = {value}"))
        #warning(f"CMS format for page cannot contain range! {key} = {value}")
      elif lkey=='author' and lvalue.count(',')>2+lvalue.count(' and '):
        warnings.setdefault("Too many commas compared to 'and':",[ ]).append((self.label,f"{key} = {value}"))
      elif lkey in duplicates:
        duplicates[lkey].setdefault(lvalue,[ ]).append((self.label,value))
      elif lkey=='journal' and value in journals: # look for misspelling
        warnings.setdefault("Misspelled journal:",[ ]).append((self.label,f"{key} = {value} -> {journals[value]}"))
      elif lkey=='volume' and value.upper().isupper():
        warnings.setdefault("CMS format of 'volume' cannot contain letter (please add to journal):",[ ]).append((self.label,f"{key} = {value}"))
      elif lkey=='volume' and self.fields.get('journal',None) in ['JHEP','J. High Energy Phys.'] and not rexp_vol_JHEP.match(value):
        warnings.setdefault("JHEP volume must be two digits (0 left padded):",[ ]).append((self.label,f"{key} = {value}"))
  
  def formatfields(self):
    """Formatting and checking items."""
    keys  = self.fields.keys()
    nkeys = len(keys)
    for i, key in enumerate(keys,1):
      lkey   = key.lower()
      value  = self.fields[key]
      lvalue = value.lower()
      if 'slaccitation' in lkey:
        value = value.upper() # capitalize everything !
      value = value.rstrip().rstrip(',') # remove extra spaces and commas
      if not i==nkeys: # do not add comma after last entry
        value += ','
      self.fields[key] = value
  
  def iterfields(self):
    """Iterate over field keys and values for writing."""
    keys = self.fields.keys()
    assert len(keys)>=1, "Found no keys... BibTeX entry empty, or too many closing braces."
    keylen = max(len(k) for k in keys)
    for i, key in enumerate(keys,1):
      row    = ""
      indent = keylen+3
      value  = self.fields[key]
      if keylen+2+len(value)>line_max:
        nmax  = line_max-keylen-3
        lines = splititem(value,nmax=nmax)
      else:
        lines = [value]
      for i, line in enumerate(lines):
        if i==0:
          row += f"  {key.ljust(keylen)} = {line}"
          if line[:2]=='"{' or line[:2]=='{{':
            indent += 1
        else:
          row += f"\n  {' '*indent} {line}"
      yield row
  
  def write(self,outfile):
    """Write BibTeX entry to given file."""
    write(outfile,self.firstline)
    for row in self.iterfields():
      write(outfile,row)
    write(outfile,self.lastline)
    return self
  

def main(args):
  """Main routine."""
  
  # USER INPUT
  infname   = args.infname
  outfname  = args.outfname
  backup    = args.backup  # make backup of original file
  check     = args.check   # check fields, and warn of potential issues
  compile   = args.compile # compile comparison files
  cmstdr    = args.cmstdr  # prepare TeX files for CMS's TDR script
  compare   = args.compare or cmstdr or compile
  verbosity = args.verbosity
  
  #### DEBUGGING
  ###infname   = "/Users/IWN/Work/tdr/notes/AN-19-019/AN-19-019.bib"
  ###outfname  = "/Users/IWN/Work/tdr/notes/AN-19-019/AN-19-019_clean.bib"
  ###check     = True
  ###cmstdr    = True # compile with CMS TDR script
  ###compare   = True
  ###compile   = True
  
  # BACKUP
  assert infname[-4:]=='.bib', f"Input file must end in .bib! Got {infname}..."
  if backup:
    import shutil
    newinfname = infname+'.bkp'
    print(f">>> Making backup {infname} -> {newinfname}")
    shutil.copy2(infname,newinfname)
    infname = newinfname # use backup as input to avoid conflict
    ###if outfname==None:
    ###  outfname = infname
  
  # SANITY CHECKS
  assert not outfname or outfname[-4:]=='.bib', f"Output file must end in .bib! Got {outfname}..."
  assert backup or infname!=outfname, "Input and output filenames cannot be the same! Otherwise use --backup to create backup of original."
  
  # LOOP OVER INPUT FILE
  labels = [ ] # labels of all references
  with open(infname,'r') as infile:
    try: #with open(outfname,'w') as outfile:
      outfile = open(outfname,'w') if outfname else None
      nwlines = 0 # number of white lines
      label = None # current label
      for line in infile:
        match = rexp_tag.search(line)
        if match: # format entry
          if nwlines>=1:
            write(outfile,'') # force white line before new BibTeX entry
          entry = Entry.fromfile(line,infile,verb=verbosity)
          entry.sortkeys()
          entry.formatfields()
          label = entry.label
          labels.append(label)
          if check:
            entry.checkfields()
          entry.write(outfile)
          nwlines = 0 # reset
        elif line.strip()=='': # empty line
          nwlines += 1
        elif line.strip()=='}': # unpaired brace
          if label:
            msg = "Unpaired closing brace"+(f" under '{label}')" if label else "")+"? BibTeX closed with too many braces?"
            raise ValueError(msg)
        else:
          ###if '%' in line[0] and nwlines>0:
          ###  print(f">>> DEBUG: nwlines={nwlines}, {line!r}")
          if nwlines>=1:
            write(outfile,'\n'*(nwlines>=2)) # write maximally two white lines
            nwlines = 0 # reset
          write(outfile,line.rstrip())
    finally: # also close on exception
      if outfile:
        outfile.close()
  print()
  
  # WRITE TEX FILE
  if compare:
    writeComparisonFiles(infname,outfname,labels,cmstdr=cmstdr,compile=compile)
  
  # WARNINGS
  if check:
    for key in duplicates: # doi, eprint
      for value in duplicates[key]:
        dupvals = duplicates[key][value] # duplicate values
        if len(dupvals)>=2:
          value0 = dupvals[0][-1]
          warnings.setdefault(f"Found duplicate {key} fields:",[ ]).append((value0,', '.join(l for l, d in dupvals)))
    if warnings:
      nwarn = sum(len(v) for k, v in warnings.items())
      print(f">>> There {'were' if nwarn>=2 else 'was'} {nwarn} warning{'s' if nwarn>=2 else ''}:")
      for warnkey in sorted(warnings):
        print(f">>> {warnkey}")
        maxlen = max(len(x[0]) for x in warnings[warnkey])+1 # longest character length
        for label, item in warnings[warnkey]:
          label = (label.strip(',')+':').ljust(maxlen)
          print(f">>>   {label} {item}")
  

if __name__ == '__main__':
  from argparse import ArgumentParser
  description = """Clean BibTeX file: key ordering, capitalization, indentation, spacing, ... and detect potential issues."""
  parser = ArgumentParser(prog="plot",description=description,epilog="Good luck!")
  parser.add_argument('infname',        help="filename of BibTeX file to reformat" )
  parser.add_argument('-o','--outfname',help="output filename of reformatted BibTeX file")
  parser.add_argument('-b','--backup',  action='store_true', help="back up original file")
  parser.add_argument('-c','--check',   action='store_true',
                                        help="check fields and warn of potential issues")
  parser.add_argument('-C','--compare', action='store_true',
                                        help="create comparison LaTeX files to validate reformatted output")
  parser.add_argument('-T','--cmstdr',  action='store_true',
                                        help="create comparison LaTeX files for CMS's TDR script")
  parser.add_argument('-x','--compile', action='store_true',
                                        help="compile comparison LaTeX files")
  parser.add_argument('-v','--verbose', dest='verbosity', type=int, nargs='?', const=1, default=0, action='store',
                                        help="set verbosity")
  args = parser.parse_args()
  main(args)
  #print(">>> Done")
  
