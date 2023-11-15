for file in *.bib; do
	echo $file
	python cleanBibTeX.py $file >> "${file/.bib/_new.bib}"
done

