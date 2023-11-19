#%%
import numpy as np
import matplotlib.pyplot as plt
import mplhep
from matplotlib import gridspec
import matplotlib.lines as lines
from matplotlib.patches import Patch
import matplotlib as mpl
mplhep.style.use("CMS")
 
 
def morphing(x,ym,y,yp):
    res=np.zeros_like(x)
    dp=yp-y
    dm=ym-y
    res[np.abs(x)<1]=((dp-dm)*x[np.abs(x)<1]+(dp+dm)*(3*x[np.abs(x)<1]**6-10*x[np.abs(x)<1]**4+15*x[np.abs(x)<1]**2)/8)/2
    res[x<-1]=-x[x<-1]*dm
    res[x>1]=x[x>1]*dp
    return res
 
 
 
x=np.linspace(-15,15,1000)



def plot(s,ax):
    #s=s*50
    m1=morphing(x,*s)
    ax.fill_between([-1,1],-50,50 , color="gray", alpha=0.15)
    ax.plot(x,s[1]+m1,color="orangered",linewidth=2.)
    ax.bar([-1],s[0],fill=False,edgecolor="blue")
    ax.bar([0],s[1],fill=False)
    ax.bar([1],s[2],fill=False,edgecolor="red")
    #ax.bar([-1,0,1],s,fill=False)
    #fill between x=-1 and x=1
    
    ax.set_ylim(0,50)
    ax.set_xlim(-2.8,2.8)
    ax.grid()
    ax.set_xticks([-2,-1,0,1,2],["-2","-1","0","+1","+2"])
    ax.tick_params(axis="y",direction="in", pad=-35,labelsize=15)
    ax.plot([1,1],[0,50],"--",color="red",linewidth=0.8,alpha=0.85)
    ax.plot([-1,-1],[0,50],"--",color="blue",linewidth=0.8,alpha=0.85)
    plt.setp(ax.get_yticklabels()[0], visible=False)
    plt.setp(ax.get_yticklabels()[-1], visible=False)
    return ax

gs = gridspec.GridSpec(2, 3,wspace=0,hspace=0.35)

fig=plt.figure(figsize=(13,10))

fig.add_artist(lines.Line2D([0.383565, 0.383565], [0.11, 0.55],color="black",linewidth=2,alpha=0.75,linestyle="--",zorder=0))

fig.add_artist(lines.Line2D([0.125, 0.125], [0.11, 0.55],color="black",linewidth=2,alpha=0.75,linestyle="--",zorder=0))

fig.add_artist(lines.Line2D([0.6420, 0.6420], [0.11, 0.55],color="black",linewidth=2,alpha=0.75,linestyle="--",zorder=0))

fig.add_artist(lines.Line2D([0.90055, 0.90055], [0.11, 0.55],color="black",linewidth=2,alpha=0.75,linestyle="--",zorder=0))


ax0 = plt.subplot(gs[0,0])
s0=np.array([18,30,35])
ax0=plot(s0,ax0)
ax0.set_ylabel(r"Bin content")


ax1=plt.subplot(gs[0,1])
s1=np.array([32,35,39])
ax1=plot(s1,ax1)
ax1.set_yticklabels([])


ax2=plt.subplot(gs[0,2])
s2=np.array([25,20,18])
ax2=plot(s2,ax2)
ax2.set_yticklabels([])

ax2.set_xlabel(r"$\theta_k$")


ax3=plt.subplot(gs[1,:])
ax3.plot([13.3333,13.3333],[0,60],"--",color="black",linewidth=2,alpha=0.75)
ax3.plot([26.6666666,26.6666666],[0,60],"--",color="black",linewidth=2,alpha=0.75)
ax3.hist(np.array([8]*s0[2]+[18]*s1[2]+[28]*s2[2]),bins=3,range=(0,40),histtype="step",color="red",linewidth=2.75,label=r"$+1\sigma$")

ax3.hist(np.array([8]*s0[1]+[18]*s1[1]+[28]*s2[1]),bins=3,range=(0,40),histtype="step",color="black",linewidth=2.75,label="Central")

ax3.hist(np.array([8]*s0[0]+[18]*s1[0]+[28]*s2[0]),bins=3,range=(0,40),histtype="step",color="blue",linewidth=2.75,label=r"$-1\sigma$")

#ax3.legend(fontsize=18,loc="upper left")

custom_lines1 = [Patch(facecolor='red', edgecolor='red',label=r"$+1\sigma$",fill=False,linewidth=2),
                Patch(facecolor='blue', edgecolor='blue',label=r"$-1\sigma$",fill=False,linewidth=2),]
legend1=ax3.legend(handles=custom_lines1,fontsize=18,bbox_to_anchor=(0.1425, 1.2875))

custom_lines2 = [Patch(facecolor='black', edgecolor='black',label=r"Center",fill=False,linewidth=2),
                lines.Line2D([0], [0], color='orangered', lw=3, label=r'$y_b+f(\theta_k,\delta_b^\pm)$'),]
legend2=ax3.legend(handles=custom_lines2,fontsize=18,bbox_to_anchor=(0.3455, 1.2875))
plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)

ax3.set_ylim(0,60)
ax3.set_xlim(0,40)
ax3.grid()

ax3.set_xticks([])
ax3.set_xticks([13.33333/2,13.333333+13.333333/2,2*13.333333+13.3333333/2],minor=True)
ax3.set_xticklabels(["Bin1","Bin2","Bin3"],minor=True)

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap
# Select a color map
cmap = mpl.cm.gist_rainbow_r
cmap=mpl.cm.Spectral_r
cmap = truncate_colormap(cmap, 0.05, 0.95)
normalize = mpl.colors.SymLogNorm(linthresh=1, linscale=1,
                                vmin=-20.0, vmax=20.0, base=2)
#normalize=mpl.colors.CenteredNorm()

m0=morphing(x,*s0)
m1=morphing(x,*s1)
m2=morphing(x,*s2)

for i in range(len(x[:-1])):
    ax3.fill_between([0,13.33333],s0[1]+m0[i],s0[1]+m0[i+1],alpha=0.2,color=cmap(normalize(x[i])))
    ax3.fill_between([13.33333,26.6666666],s1[1]+m1[i],s1[1]+m1[i+1],alpha=0.2,color=cmap(normalize(x[i])))
    ax3.fill_between([26.66666666,39.999999],s2[1]+m2[i],s2[1]+m2[i+1],alpha=0.2,color=cmap(normalize(x[i])))


cbax = fig.add_axes([0.925, 0.12, 0.025, 0.75])
cb = mpl.colorbar.ColorbarBase(cbax, cmap=cmap, norm=normalize, orientation='vertical',alpha=0.5)
cb.set_label(r"$\theta_k$", rotation=0, labelpad=5,loc="center",fontsize=35)
cb.set_ticks([-16,-8,-4,-2,-1,0,1,2,4,8,16])
cb.set_ticklabels(["-16","-8","-4","-2","-1","0","+1","+2","+4","+8","+16"])

#https://stackoverflow.com/questions/11564273/continuous-colormap-fill-between-two-lines

xN=np.random.normal(0,1,10000000)
def posterior(s):
    r=s[1]+morphing(xN,*s)
    h=np.histogram(r,bins=250,density=True)
    hx=h[1][:-1]+(h[1][1:]-h[1][:-1])/2
    h[0][hx<0]=0
    hy=h[0]
    
    #hx=hx[hy>1e-3]
    #hy=hy[hy>1e-3]
    return hx,hy

hx0,hy0=posterior(s0)
#ax3.plot(0.1+0.2+hy0*100,hx0,color="grey",linewidth=2.5,zorder=1,label=r"$f(\theta_k,\delta_b^\pm) \; \theta \sim \pi_k(\theta_k)$")

ax3.fill_betweenx(hx0,0,hy0*100,color="white",zorder=1,edgecolor="grey",linewidth=2.5)

hx1,hy1=posterior(s1)

ax3.fill_betweenx(hx1,13.3333,13.3333+hy1*80,color="white",zorder=1,edgecolor="grey",linewidth=2.5)


hx2,hy2=posterior(s2)
ax3.fill_betweenx(hx2,26.6666,26.6666+hy2*50,color="white",zorder=1,edgecolor="grey",linewidth=2.5)

"""
ax3.plot(0.1+np.array([0.2,0.2]),[47,60],color="grey",zorder=1,linewidth=1.5)
ax3.plot(0.1+np.array([13.5,13.5]),[50,60],color="grey",zorder=1,linewidth=1.5)
ax3.plot(0.1+np.array([13.5,13.5]),[0,20],color="grey",zorder=1,linewidth=1.5)
ax3.plot(0.1+np.array([26.8,26.8]),[45,60],color="grey",zorder=1,linewidth=1.5)
ax3.plot(0.1+np.array([26.8,26.8]),[0,10],color="grey",zorder=1,linewidth=1.5) """

custom_lines3 = [
                lines.Line2D([0], [0], color='white', lw=3, label=r'$y_b+f(\theta_k,\delta_b^\pm)  \quad \theta_{k} \sim \pi_k(\theta_k)$'),
                ]

custom_lines3=[Patch(facecolor='white', edgecolor='grey',label=r"$y_b+f(\theta_k,\delta_b^\pm) \quad \theta_k \sim \pi_k(\theta_k)$",fill=True,linewidth=2.5),]
ax3.legend(handles=custom_lines3,fontsize=16.5,labelcolor="black",loc="upper right")
ax3.tick_params(axis="y",zorder=10)

ax3b = ax3.twiny()
#small ticks
ax3b.set_xticks([])

t1=(np.linspace(0.3,12,4))
t2=(np.linspace(13.6,25.3,4))
t3=(np.linspace(26.9,38.6,4))
t=np.linspace(0,39.99,20)
l1=(t1-0.2)/100
l2=(t2-13.5)/80
l3=(t3-26.8)/50

t1=t1.tolist()
t2=t2.tolist()
t3=t3.tolist()
l1=l1.tolist()
l2=l2.tolist()
l3=l3.tolist()

ax3b.set_xticks(t,minor=True)
ax3b.tick_params(axis="x",direction="in", pad=-25,labelsize=15,labelcolor="grey",which="minor",colors='white')
ax3b.set_xlabel("a.u.",fontsize=15,labelpad=-15,color="white")

plt.savefig('morph.pdf',bbox_inches='tight')
# %%
