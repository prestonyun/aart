from aart_func import *
from params import * 

print("Intensity")

fnbands=path+"LensingBands_a_%s_i_%s.h5"%(spin_case,i_case)

print("Reading file: ",fnbands)

h5f = h5py.File(fnbands,'r')

supergrid0=h5f['grid0'][:]
mask0=h5f['mask0'][:]
N0=int(h5f["N0"][0])

if bvapp!=1:

	supergrid1=h5f['grid1'][:]
	mask1=h5f['mask1'][:]
	N1=int(h5f["N1"][0])

	supergrid2=h5f['grid2'][:]
	mask2=h5f['mask2'][:]
	N2=int(h5f["N2"][0])

	fnbands=path+"Rays_a_%s_i_%s.h5"%(spin_case,i_case)

	print("Reading file: ",fnbands)

	h5f = h5py.File(fnbands,'r')

	rs0=h5f['rs0'][:]
	sign0=h5f['sign0'][:]
	rs1=h5f['rs1'][:]
	sign1=h5f['sign1'][:]
	rs2=h5f['rs2'][:]
	sign2=h5f['sign2'][:]
	h5f.close()

	obsint.br(supergrid0,mask0,N0,rs0,sign0,supergrid1,mask1,N1,rs1,sign1,supergrid2,mask2,N2,rs2,sign2)

else:

	h5f.close()

	fnrays=path+"Rays_bv_a_%s_i_%s.h5"%(spin_case,i_case)
	print("Reading file: ",fnrays)

	h5f = h5py.File(fnrays,'r')

	rs0_bv=h5f['rs0_bv'][:]
	sign0_bv=h5f['sign0_bv'][:]

	h5f.close()

	obsint.br_bv(supergrid0,mask0,N0,rs0_bv,sign0_bv)	
