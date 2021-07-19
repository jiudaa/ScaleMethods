import numpy as np
import pandas as pd

REF = 100  #set reference frame

def BSScale(dfX,dfY,df_box):
    '''box scale for gait skeleton video
    Args:
        dfX: a DataFrame of x location before scaling
        dfY: a DataFrame of y location before scaling
        df_box: a DataFrame of bounding box

    Returns:
        X: a DataFrame of x location after scaling
        Y: a DataFrame of y location after scaling
        ratio: a list of all ratios

    '''
    X=pd.DataFrame(columns=dfX.columns)
    Y=pd.DataFrame(columns=dfY.columns)
    w,h=int(df_box.iloc[REF][2]),int(df_box.iloc[REF][3])
    ratio=[]
    for ind in range(len(dfX)):
        bbox=[int(i) for i in df_box[ind]]
        x= dfX.iloc[ind,:]-(bbox[0]-1)
        y= dfY.iloc[ind,:]-(bbox[1]-1)
        box = [bbox[0], bbox[0]+bbox[2], bbox[1], (bbox[1]+bbox[3])]
        w00,h00=abs(int(x.RShoulder-x.LShoulder)),abs(int(y.RShoulder-y.LShoulder))
        ratio_x = w/bbox[2]
        ratio_y = h/bbox[3]
        x1=ratio_x*x
        y1=ratio_y*y
        X=X.append(x1)
        Y=Y.append(y1)
        ratio.append([ratio_x,ratio_x])
    return X,Y,ratio


def LSRHScale(dfX,dfY,df_box):
    X=pd.DataFrame(columns=dfX.columns)
    Y=pd.DataFrame(columns=dfY.columns)
    s_w,s_h = abs(int(dfX.iloc[REF].RShoulder-dfX.iloc[REF].LShoulder))+1,abs(int(dfY.iloc[REF].RShoulder-dfY.iloc[REF].LShoulder))+1
    h_w,h_h = abs(int(dfX.iloc[REF].LShoulder-dfX.iloc[REF].RHip))+1,abs(int(dfY.iloc[REF].LShoulder-dfY.iloc[REF].RHip))+1
    ratio=[]
    for ind in range(len(dfX)):
        bbox=[int(i) for i in df_box[ind]]
        x= dfX.iloc[ind,:]-(bbox[0]-5)
        y= dfY.iloc[ind,:]-(bbox[1]-5)
        box = [bbox[0], bbox[0]+bbox[2], bbox[1], (bbox[1]+bbox[3])]
        w00,h00=abs(int(x.LShoulder-x.RHip))+1,abs(int(y.LShoulder-y.RHip))+1
        x1=((h_w/w00))*x
        y1=((h_h/h00))*y
        X=X.append(x1)
        Y=Y.append(y1)
        ratio.append([h_w/w00,h_h/h00])
    return dfxx,dfyy,ratio

def LSRH_d(dfX,dfY,df_box):
    X=pd.DataFrame(columns=dfX.columns)
    Y=pd.DataFrame(columns=dfY.columns)
    r_l = np.sqrt(np.power((dfX.iloc[REF].RShoulder-dfX.iloc[REF].LHip),2)+np.power((dfY.iloc[REF].RShoulder-dfY.iloc[REF].LHip),2))
    ratio=[]
    for ind in range(len(dfX)):
        bbox=[int(i) for i in df_box[ind]]
        x= dfX.iloc[ind,:]
        y= dfY.iloc[ind,:]
        length=np.sqrt(np.power((x.RShoulder-x.LHip),2)+np.power((y.RShoulder-y.LHip),2))
        box =[bbox[0], bbox[0]+bbox[2], bbox[1], (bbox[1]+bbox[3])]
        factor=r_l/length
        x=factor*x
        y=factor*y
        X=X.append(x)
        Y=Y.append(y)
        ratio.append([factor,factor])
    return X,Y,ratio



def SScale(dfX,dfY,df_box):
    X=pd.DataFrame(columns=dfX.columns)
    Y=pd.DataFrame(columns=dfY.columns)
    h_w,h_h = abs(int(dfX.iloc[REF].LShoulder-dfX.iloc[REF].RShoulder))+1,abs(int(dfY.iloc[REF].LShoulder-dfY.iloc[REF].RShoulder))+1
    ratio=[]
    for ind in range(len(dfX)):
        bbox=[int(i) for i in df_box[ind]]
        x= dfX.iloc[ind,:]-(bbox[0]-5)
        y= dfY.iloc[ind,:]-(bbox[1]-5)
        box = [bbox[0], bbox[0]+bbox[2], bbox[1], (bbox[1]+bbox[3])]
        w00,h00=abs(int(x.LShoulder-x.RShoulder))+1,abs(int(y.LShoulder-y.RShoulder))+1
        x=((h_w/w00))*x
        y=((h_h/h00))*y
        X=X.append(x)
        Y=Y.append(y)
        ratio.append([h_w/w00,h_h/h00])
    return X,Y,ratio

def HScale(dfX,dfY,df_box):
    X=pd.DataFrame(columns=dfX.columns)
    Y=pd.DataFrame(columns=dfY.columns)
    h_w,h_h = abs(int(dfX.iloc[REF].LHip-dfX.iloc[REF].RHip))+1,abs(int(dfY.iloc[REF].LHip-dfY.iloc[REF].LHip))+1
    ratio= []
    for ind in range(len(dfX)):
        bbox=[int(i) for i in df_box[ind]]
        x= dfX.iloc[ind,:]-(bbox[0]-1)
        y= dfY.iloc[ind,:]-(bbox[1]-1)
        box = [bbox[0], bbox[0]+bbox[2], bbox[1], (bbox[1]+bbox[3])]
        w00,h00=abs(int(x.LHip-x.RHip))+1,abs(int(y.LHip-y.RHip))+1
        ratio_x = h_w/w00
        ratio_y = h_h/h00 
        x=ratio_x*x
        y=ratio_y*y
        X=X.append(x)
        Y=Y.append(y)
        ratio.append([ratio_x,ratio_y])
    return X,Y,ratio

def ShouderHeiScale(dfX,dfY,df_box):
    X=pd.DataFrame(columns=dfX.columns)
    Y=pd.DataFrame(columns=dfY.columns)
    s_w,s_h = abs(int(dfX.iloc[REF].RShoulder-dfX.iloc[REF].LShoulder))+1,abs(int(dfY.iloc[REF].RShoulder-dfY.iloc[REF].LShoulder))+1
    w,h=int(df_box.iloc[ref][2]),int(df_box.iloc[ref][3])
    ratio=[]
    for ind in range(len(dfX)):
        bbox=[int(i) for i in df_box[ind]]
        x= dfX.iloc[ind,:]-(bbox[0]-5)
        y= dfY.iloc[ind,:]-(bbox[1]-5)
        box = [bbox[0], bbox[0]+bbox[2], bbox[1], (bbox[1]+bbox[3])]
        w00,h00=abs(int(x.RShoulder-x.LShoulder))+1,abs(int(y.RShoulder-y.LShoulder))+1
        x1=((s_w/w00))*x
        y1=((h/bbox[3]))*y
        X=X.append(x1)
        Y=Y.append(y1)
        ratio.append([s_w/w00,h/bbox[3]])
    return X,Y,ratio
