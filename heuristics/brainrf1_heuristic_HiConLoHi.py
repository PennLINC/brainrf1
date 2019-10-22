#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS with HiConLoHi stimulation condition visits"""
import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

    
# **********************************************************************************
# tms session

# condition (run 1)
nback_HiConLoHiWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConLoHiWMgated_run-01_bold')    
 
# condition (run 2)   
nback_HiConLoHiWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConLoHiWMgated_run-02_bold')   

# iTBS
iTBS_gated = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}'
    '_task-iTBS_acq-gated_bold')

# field map, topup style      
fmap_pa_tms_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fMRIdistmap_dir-PA_run-01_epi')
fmap_pa_tms_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fMRIdistmap_dir-PA_run-02_epi')  

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
        nback_HiConLoHiWMgated_run1: [],
        iTBS_gated: [],
        nback_HiConLoHiWMgated_run2: [],
        
        fmap_pa_tms_run1: [],
        fmap_pa_tms_run2: [],
    }
    
    for s in seqinfo:
        protocol = s.protocol_name.lower()

        # TMS day  
        if "acq-fMRIdistmap_dir-PA_run-01" in s.protocol_name:
            info[fmap_pa_tms_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-02" in s.protocol_name:
            info[fmap_pa_tms_run2].append(s.series_id)
        
        elif "task-nback_acq-HiConLoHiWMgated_run-01" in s.protocol_name:
            info[nback_HiConLoHiWMgated_run1].append(s.series_id)
            
        elif "task-iTBS_acq-gated_bold" in s.protocol_name:
            info[iTBS_gated].append(s.series_id)    
        
        elif "task-nback_acq-HiConLoHiWMgated_run-02" in s.protocol_name:
            info[nback_HiConLoHiWMgated_run2].append(s.series_id)

    return info


# Any extra metadata that might not be automatically added by dcm2niix

IntendedFor = {
    
    # HiConLoHi    
    fmap_pa_tms_run1: [ '{session}/func/sub-{subject}_{session}_task-nback_acq-HiConLoHiWMgated_run-01_bold.nii.gz',
                        '{session}/func/sub-{subject}_{session}_task-iTBS_acq-gated_bold.nii.gz'],
    fmap_pa_tms_run2:[ '{session}/func/sub-{subject}_{session}_task-nback_acq-HiConLoHiWMgated_run-02_bold.nii.gz'],
    }
