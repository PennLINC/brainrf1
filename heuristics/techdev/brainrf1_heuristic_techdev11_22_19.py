#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS for 11.22.19 techdev"""
import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

    
# **********************************************************************************
# t1

t1w = create_key(
    'sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')

# condition (run 1)
nback_HiConHiLoWMgated1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated1_bold')   
nback_HiConHiLoWMgated2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated2_bold')    

# **********************************************************************************

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    last_run = len(seqinfo)

    info = {

        # TMS scans
        t1w: [],
        nback_HiConHiLoWMgated1: [],
        nback_HiConHiLoWMgated2: [],
    }
    
    for s in seqinfo:
        protocol = s.protocol_name.lower()

        # TMS day  
        if "t1w" in protocol:
            info[t1w].append(s.series_id)
        elif "2019-11-22T08:36:37.085000" in s.date:
            info[nback_HiConHiLoWMgated1].append(s.series_id)
        elif "2019-11-22T08:53:43.490000" in s.date:
            info[nback_HiConHiLoWMgated2].append(s.series_id)
    return info


# Any extra metadata that might not be automatically added by dcm2niix.

IntendedFor = {
    
    # HiConHiLo    
    }
