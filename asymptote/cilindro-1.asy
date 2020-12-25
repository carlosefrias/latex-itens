if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="cilindro-1";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

//
// Global Asymptote definitions can be put here.
//
usepackage("bm");
texpreamble("\def\V#1{\bm{#1}}");

import solids;
size(0,100);

revolution r=cylinder(O,1,1.5,Y+Z);
draw(r,heavygreen);
