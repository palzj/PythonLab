#  import arcpy

# arcpy.Union_analysis("F:\\LPS_mb\\LPS_jtgx.gdb\\TL_b #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\JC_b #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_GS #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_YJ #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_EJ #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_SHJ #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_SJ #;"
#                      "F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_WJ #", JT_pjjg, "ALL", "", "GAPS")


def Test():
    ms = "F:\\LPS_mb\\LPS_jtgx.gdb\\TL_b #;"
    index = ms.rindex("\\")
    xs = ms[0:index]
    print xs