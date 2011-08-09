from SimpleCV.base import *
from SimpleCV.Features import Feature, FeatureSet
from SimpleCV.ColorModel import ColorModel
from SimpleCV.Color import Color
from SimpleCV.ImageClass import Image
from SimpleCV.BlobMaker import BlobMaker
from SimpleCV.SegmentationBase import SegmentationBase

import abc


class ColorSegmentation(SegmentationBase):
    mColorModel = []
    mError = False
    mCurImg = []
    mTruthImg = []
    mBlobMaker = []
    
    def __init__(self):
        self.mColorModel = ColorModel()
        self.mError = False
        self.mCurImg = Image()
        self.mTruthImg = Image()
        self.mBlobMaker = BlobMaker()
 
    def loadSettings(self, file):       
        """
        Load all of the segmentation settings from file
        """
        self.mColorModel.load(file)
        return
    
    def saveSettings(self, file):
        """
        save all of the segmentation settings from file
        """
        self.mColorModel.save(file)
        return
    
    def addImage(self, img):
        """
        Add a single image to the segmentation algorithm
        """
        self.mTruthImg = img
        self.mCurImg = self.mColorModel.threshold(img)
        return
    

    def isReady(self):
        """
        Returns true if the camera has a segmented image ready. 
        """
        return True;
    
    def isError(self):
        """
        Returns true if the segmentation system has detected an error.
        Eventually we'll consruct a syntax of errors so this becomes
        more expressive 
        """
        return self.mError #need to make a generic error checker
    
    def resetError(self):
        """
        Clear the previous error. 
        """
        self.mError = false
        return 

    def reset(self):
        """
        Perform a reset of the segmentation systems underlying data.
        """
        self.mColorModel.reset()
    
    def getSegmentedImage(self, whiteFG=True):
        """
        Return the segmented image with white representing the foreground
        and black the background. 
        """
        return self.mCurImg
 
    def getSetmentedBlobs(self):
        """
        return the segmented blobs from the fg/bg image
        """
        return self.mBlobMaker.extractFromBinary(self.mCurImg,self.mTruthImg)
        
    # The following are class specific methods
    
    def addToModel(self, data):
        self.mColorModel.add(data)
    
    def subtractModel(self, data):
        self.mColorModel.remove(data)
    
    