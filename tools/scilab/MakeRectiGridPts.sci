function [x,y,z]=MakeRectiGridPts(xmin,xmax,dx,ymin,ymax,dy,zmin,zmax,dz,posdir,ptsname)
// (c) Maureen Clerc, April 2008
ptsfile=posdir+ptsname;
vtkfile=ptsfile+'.vtk';
ptsdxfile=ptsfile+'dx';
ptsdyfile=ptsfile+'dy';
ptsdzfile=ptsfile+'dz';

x=xmin:dx:xmax;
y=ymin:dy:ymax;
z=zmin:dz:zmax;
nx=length(x);
ny=length(y);
nz=length(z);
if nz==1
  xx = x'*ones(1,ny);
  yy = ones(nx,1)*y;
  zz = zmin*ones(nx,ny);
elseif nx ==1
  yy = y'*ones(1,nz);
  zz = ones(ny,1)*z;
  xx = xmin*ones(ny,nz);
elseif ny ==1
  zz = z'*ones(1,nx);
  xx = ones(nz,1)*x;
  yy = ymin*ones(nz,nx);
else disp('Error: one of the three dimensions must be equal to 1.')
end
savevtkrectigrid(vtkfile,x,y,z);
// dimensions of the grid np1 * np2
[np1,np2] =  size(zz);
np = np1*np2
pt = zeros(np,3);
pt(:,1) = matrix(xx,[np 1]);
pt(:,2) = matrix(yy,[np 1]);
pt(:,3) = matrix(zz,[np 1]);
fprintfMat(ptsfile,pt);
newpt = pt;
newpt(:,1) = newpt(:,1)+0.001;
fprintfMat(ptsdxfile,newpt);
newpt = pt;
newpt(:,2) = newpt(:,2)+0.001;
fprintfMat(ptsdyfile,newpt);
newpt = pt;
newpt(:,3) = newpt(:,3)+0.001;
fprintfMat(ptsdzfile,newpt);

