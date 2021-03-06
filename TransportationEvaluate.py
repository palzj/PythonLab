# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TransportationEvaluate.py
# Created on: 2017-09-26 10:02:06.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: 交通干线 <LCA> <LRRL> <LRDL>
# Description:
# 根据地理国情普查成果进行交通干线影响评价分析。
#   第一，通过LAC地表覆盖分类数据抽取机场范围进行评价分析；
#   第二，利用LRRL铁路要素，LRDL公路要素的不同道路等级进行评价分析。
#   评价结果越高，说明交通干线影响越大，空间开发适宜性越高。

# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

def ExcuteEvaluate(lca,lrrl,lrdl):
    # Script arguments
    LCA = lca
    LRRL = lrrl
    LRDL = lrdl

    # Local variables:
    TL_b = LRRL
    TL_b_shp__5_ = TL_b
    TL_b_shp__4_ = TL_b_shp__5_
    TL_b_shp__2_ = TL_b_shp__4_
    JT_pjjg = TL_b_shp__2_
    JT_union_shp__4_ = JT_pjjg
    JC = LCA
    JCFC = JC
    JC_b_shp = JCFC
    LRDL_GS = LRDL
    LRDL_GS__2_ = LRDL_GS
    LRDL_GS_shp__4_ = LRDL_GS__2_
    LRDL_YJ = LRDL
    LRDL_YJ__2_ = LRDL_YJ
    LRDL_YJ_shp__4_ = LRDL_YJ__2_
    LRDL_EJ = LRDL
    LRDL_EJ__2_ = LRDL_EJ
    LRDL_EJ_shp__4_ = LRDL_EJ__2_
    LRDL_SHJ = LRDL
    LRDL_SHJ__2_ = LRDL_SHJ
    LRDL_SHJ_shp__3_ = LRDL_SHJ__2_
    LRDL_SJ = LRDL
    LRDL_SJ__2_ = LRDL_SJ
    LRDL_SJ_shp__3_ = LRDL_SJ__2_
    LRDL_WJ = LRDL
    LRDL_WJ__2_ = LRDL_WJ
    LRDL_WJ_shp__4_ = LRDL_WJ__2_

    try:
        # Process: 多环缓冲区 (2)
        arcpy.MultipleRingBuffer_analysis(LRRL, TL_b, "3;6", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段
        arcpy.AddField_management(TL_b, "TL_PJDJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段
        arcpy.CalculateField_management(TL_b_shp__5_, "TL_PJDJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 5\\n  elif (WellYield ==6):\\n    return 4\\n\\n")

        # Process: 计算字段 (3)
        arcpy.CalculateField_management(TL_b_shp__4_, "TL_PJDJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 5\\n  elif (WellYield ==6):\\n    return 4\\n\\n\\n")

        # Process: 创建要素图层
        arcpy.MakeFeatureLayer_management(LCA, JC, "CC = '0714'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;SHAPE SHAPE VISIBLE NONE;CC CC VISIBLE NONE;TAG TAG VISIBLE NONE;SHAPE_Length SHAPE_Length VISIBLE NONE;SHAPE_Area SHAPE_Area VISIBLE NONE;FLMC FLMC VISIBLE NONE")

        # Process: 多环缓冲区
        arcpy.MultipleRingBuffer_analysis(JC, JCFC, "30;60", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (2)
        arcpy.AddField_management(JCFC, "JC_PJDJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (2)
        arcpy.CalculateField_management(JC_b_shp, "JC_PJDJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield == 30):\\n    return 4\\n  elif (WellYield== 60):\\n    return 3\\n")

        # Process: 创建要素图层 (2)
        arcpy.MakeFeatureLayer_management(LRDL, LRDL_GS, "RTEG = '高速'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;CC CC VISIBLE NONE;GB GB VISIBLE NONE;DEST DEST VISIBLE NONE;NAME NAME VISIBLE NONE;RN RN VISIBLE NONE;SDTF SDTF VISIBLE NONE;START START VISIBLE NONE;TYPE TYPE VISIBLE NONE;BLDTM BLDTM VISIBLE NONE;ELEVT ELEVT VISIBLE NONE;RNP RNP VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE")

        # Process: 多环缓冲区 (3)
        arcpy.MultipleRingBuffer_analysis(LRDL_GS, LRDL_GS__2_, "3;6", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (3)
        arcpy.AddField_management(LRDL_GS__2_, "LRDL_GS_DJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (4)
        arcpy.CalculateField_management(LRDL_GS_shp__4_, "LRDL_GS_DJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 5\\n  elif (WellYield ==6):\\n    return 4\\n\\n\\n")

        # Process: 创建要素图层 (3)
        arcpy.MakeFeatureLayer_management(LRDL, LRDL_YJ, "RTEG = '一级'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;CC CC VISIBLE NONE;GB GB VISIBLE NONE;DEST DEST VISIBLE NONE;NAME NAME VISIBLE NONE;RN RN VISIBLE NONE;SDTF SDTF VISIBLE NONE;START START VISIBLE NONE;TYPE TYPE VISIBLE NONE;BLDTM BLDTM VISIBLE NONE;ELEVT ELEVT VISIBLE NONE;RNP RNP VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE")

        # Process: 多环缓冲区 (4)
        arcpy.MultipleRingBuffer_analysis(LRDL_YJ, LRDL_YJ__2_, "3;6", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (4)
        arcpy.AddField_management(LRDL_YJ__2_, "LRDL_YJ_DJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (5)
        arcpy.CalculateField_management(LRDL_YJ_shp__4_, "LRDL_YJ_DJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 4\\n  elif (WellYield ==6):\\n    return 3\\n\\n")

        # Process: 创建要素图层 (4)
        arcpy.MakeFeatureLayer_management(LRDL, LRDL_EJ, "RTEG = '二级'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;CC CC VISIBLE NONE;GB GB VISIBLE NONE;DEST DEST VISIBLE NONE;NAME NAME VISIBLE NONE;RN RN VISIBLE NONE;SDTF SDTF VISIBLE NONE;START START VISIBLE NONE;TYPE TYPE VISIBLE NONE;BLDTM BLDTM VISIBLE NONE;ELEVT ELEVT VISIBLE NONE;RNP RNP VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE")

        # Process: 多环缓冲区 (5)
        arcpy.MultipleRingBuffer_analysis(LRDL_EJ, LRDL_EJ__2_, "3;6", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (5)
        arcpy.AddField_management(LRDL_EJ__2_, "LRDL_EJ_DJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (6)
        arcpy.CalculateField_management(LRDL_EJ_shp__4_, "LRDL_EJ_DJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 3\\n  elif (WellYield ==6):\\n    return 2\\n\\n\\n")

        # Process: 创建要素图层 (5)
        arcpy.MakeFeatureLayer_management(LRDL, LRDL_SHJ, "RTEG = '三级'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;CC CC VISIBLE NONE;GB GB VISIBLE NONE;DEST DEST VISIBLE NONE;NAME NAME VISIBLE NONE;RN RN VISIBLE NONE;SDTF SDTF VISIBLE NONE;START START VISIBLE NONE;TYPE TYPE VISIBLE NONE;BLDTM BLDTM VISIBLE NONE;ELEVT ELEVT VISIBLE NONE;RNP RNP VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE")

        # Process: 多环缓冲区 (6)
        arcpy.MultipleRingBuffer_analysis(LRDL_SHJ, LRDL_SHJ__2_, "3;6", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (6)
        arcpy.AddField_management(LRDL_SHJ__2_, "LRDLSHJ_DJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (7)
        arcpy.CalculateField_management(LRDL_SHJ_shp__3_, "LRDLSHJ_DJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 2\\n  elif (WellYield ==6):\\n    return 1\\n\\n\\n")

        # Process: 创建要素图层 (6)
        arcpy.MakeFeatureLayer_management(LRDL, LRDL_SJ, "RTEG = '四级'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;CC CC VISIBLE NONE;GB GB VISIBLE NONE;DEST DEST VISIBLE NONE;NAME NAME VISIBLE NONE;RN RN VISIBLE NONE;SDTF SDTF VISIBLE NONE;START START VISIBLE NONE;TYPE TYPE VISIBLE NONE;BLDTM BLDTM VISIBLE NONE;ELEVT ELEVT VISIBLE NONE;RNP RNP VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE")

        # Process: 多环缓冲区 (7)
        arcpy.MultipleRingBuffer_analysis(LRDL_SJ, LRDL_SJ__2_, "3", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (7)
        arcpy.AddField_management(LRDL_SJ__2_, "LRDL_SJ_DJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (8)
        arcpy.CalculateField_management(LRDL_SJ_shp__3_, "LRDL_SJ_DJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 1\\n\\n\\n\\n")

        # Process: 创建要素图层 (7)
        arcpy.MakeFeatureLayer_management(LRDL, LRDL_WJ, "RTEG = '五级'", "",
                                          "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;CC CC VISIBLE NONE;GB GB VISIBLE NONE;DEST DEST VISIBLE NONE;NAME NAME VISIBLE NONE;RN RN VISIBLE NONE;SDTF SDTF VISIBLE NONE;START START VISIBLE NONE;TYPE TYPE VISIBLE NONE;BLDTM BLDTM VISIBLE NONE;ELEVT ELEVT VISIBLE NONE;RNP RNP VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE")

        # Process: 多环缓冲区 (8)
        arcpy.MultipleRingBuffer_analysis(LRDL_WJ, LRDL_WJ__2_, "3", "Kilometers", "distance", "ALL", "FULL")

        # Process: 添加字段 (8)
        arcpy.AddField_management(LRDL_WJ__2_, "LRDL_WJ_DJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (9)
        arcpy.CalculateField_management(LRDL_WJ_shp__4_, "LRDL_WJ_DJ", "Reclass( !distance! )", "PYTHON_9.3",
                                        "def Reclass(WellYield):\\n  if (WellYield ==3):\\n    return 1\\n\\n\\n")

        # Process: 联合
        # arcpy.Union_analysis(
        #     "F:\\LPS_mb\\LPS_jtgx.gdb\\TL_b #;F:\\LPS_mb\\LPS_jtgx.gdb\\JC_b #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_GS #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_YJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_EJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_SHJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_SJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_WJ #",
        #     JT_pjjg, "ALL", "", "GAPS")

        ms = lca
        index = ms.rindex("\\")
        xs = ms[0:index]
        tstr = "F:\\LPS_mb\\LPS_jtgx.gdb\\TL_b #;F:\\LPS_mb\\LPS_jtgx.gdb\\JC_b #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_GS #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_YJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_EJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_SHJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_SJ #;F:\\LPS_mb\\LPS_jtgx.gdb\\LRDL_WJ #"
        tstr = tstr.replace("F:\\LPS_mb\\LPS_jtgx.gdb",xs)
        arcpy.Union_analysis( tstr, JT_pjjg, "ALL", "", "GAPS")

        # Process: 添加字段 (9)
        arcpy.AddField_management(JT_pjjg, "JTGXPJ", "SHORT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: 计算字段 (10)
        arcpy.CalculateField_management(JT_union_shp__4_, "JTGXPJ",
                                        "!TL_PJDJ! + !JC_PJDJ! + !LRDL_GS_DJ! + !LRDL_YJ_DJ! + !LRDL_EJ_DJ! + !LRDLSHJ_DJ! + !LRDL_SJ_DJ! + !LRDL_WJ_DJ!",
                                        "PYTHON_9.3", "")
        return 1
    except:
        return 0

