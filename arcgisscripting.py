'''----------------------------------------------------------------------------------
 arcgisscripting.py
 Version:       0.9.1
 Author:        Philippe Le Grand
 Required Argumuments:  None
 Description:	This module serves to replace ESRI's arcgisscripting.dll
 				on configurations where it is not available

	This script is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

   A copy of the GNU General Public License may be obtained
   online at

	   http://www.gnu.org/copyleft/gpl.html

   or by writing to the

	   Free Software Foundation, Inc.,
	   51 Franklin Street, Fifth Floor,
	   Boston, MA  02110-1301  USA

----------------------------------------------------------------------------------'''

import win32com.client
import win32com.client.gencache
def create(licensetype=None):
	gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")
	if licensetype is not None:
		Licensed=gp.SetProduct(licensetype)
		if not (Licensed in ["NotLicensed","Failed"]):
			return gp
	#Either the licensetype was not set, or it failed
	#Try to get the highest possible license
	types = ["ArcInfo","ArcEditor","ArcView"]
	for license in types:
		Licensed=gp.CheckProduct(license)
		if not (Licensed in ["NotLicensed","Failed"]):
			Licensed = gp.SetProduct(license)
			print "geoprocessor started with license: %s (%s)"%(license,Licensed)
			return gp
		else:
			print "license %s is %s"%(license,Licensed)
	gp.AddError("No License available for geoprocessor")
	raise ValueError,"No License available for geoprocessor"

if (__name__=="__main__"):
	gp=create()