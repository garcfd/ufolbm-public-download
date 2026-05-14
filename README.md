This code was developed from the 2D Python code of Jonas Latt (unige coursera). The executables here were compiled with Nvidia pgf90 Fortran. Lots of work has gone into the development of this LBM solver, mainly converting it from 2D Python, to 3D Fortran and making it run on Nvidia GPUs. Making it suitable for high speed flows, adding turbulence model, and free-slip wall boundary. The compiler generates executable versions (host/multi/gpu). The gpu version compiled with gpu=ccall, so it should run on any Nvidia gpu. The solver imports STL files, and so can use arbitrary 3D geometry. The code uses RLBM 'regularised' LBM method for high reynold number flows. Work has also been used from Navin M. Sangtani Lakhwani thesis (p55) and from Moritz Lehmann pdf notes on LinkedIn. You will obviously need a NVIDIA GPU if you want to run the GPU version, but the other 2 versions (basic and multicore) will run fine on just CPU. Recent work has focussed on developing a reflection matrix which can be used to model free-slip walls on arbitrary surfaces. Have a look on Youtube and Twitter/X for details of "garcfd" + "LBM" work where you will find many examples and demos.

Note: tang=0 mean 'bounce-back' is used by default.  
If tang=1 then the tangential wall boundary is used.  
If tang=1, then the wlfn value specifies the 'reach'.  


