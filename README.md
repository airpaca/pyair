# PyAir

PyAir provides facilities :

 - for the connection to the ISEO XAIR database, and for getting values/informations
 - in the computation of Air Quality values for the French reglementation,



Typical usage with Python 2.7 or Python 3.x :

    #!/usr/bin/env python

    import pyair
    xr = pyair.xair.XAIR(user, pwd, ip, port, base)
    df = xr.get_mesures(mes=["O3_AA", "O3_BB"])
    pyair.reg.aot40_vegetation(df)

Look at http://pythonhosted.org/PyAir/ for an example
