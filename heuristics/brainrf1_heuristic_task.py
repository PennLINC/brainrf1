#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS for Task Visit"""
import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

# field maps
fmap_pa_task_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fMRIdistmap_dir-PA_run-01_epi')
fmap_pa_task_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fMRIdistmap_dir-PA_run-02_epi')
fmap_pa_task_run3 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_acq-fMRIdistmap_dir-PA_run-03_epi')

# flanker
flanker_bold = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-flanker_bold')
    
# graph learning
graphlearning_bold_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-01_bold')
graphlearning_bold_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-02_bold')    
graphlearning_bold_run3 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-03_bold')
graphlearning_bold_run4 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-04_bold')
graphlearning_bold_run5 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-05_bold')

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
        # task
        fmap_pa_task_run1: [],
        fmap_pa_task_run2: [],
        fmap_pa_task_run3: [], 
        
        flanker_bold: [],
        graphlearning_bold_run1: [],
        graphlearning_bold_run2: [],
        graphlearning_bold_run3: [],
        graphlearning_bold_run4: [],
        graphlearning_bold_run5: [],
    }
    
    for s in seqinfo:
        protocol = s.protocol_name.lower()

        # Task day
        if "acq-fMRIdistmap_dir-PA_run-01" in s.protocol_name:
            info[fmap_pa_task_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-02" in s.protocol_name:
            info[fmap_pa_task_run2].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-03" in s.protocol_name:
            info[fmap_pa_task_run3].append(s.series_id)
        
        # PMUs not found, how to differentiate if located
        elif "task-flanker_bold" in s.protocol_name:
            info[flanker_bold].append(s.series_id)
        
        elif "task-graphlearning_run-01" in s.protocol_name:
            info[graphlearning_bold_run1].append(s.series_id)
        elif "task-graphlearning_run-02" in s.protocol_name:
            info[graphlearning_bold_run2].append(s.series_id)
        elif "task-graphlearning_run-03" in s.protocol_name:
            info[graphlearning_bold_run3].append(s.series_id)
        elif "task-graphlearning_run-04" in s.protocol_name:
            info[graphlearning_bold_run4].append(s.series_id)
        elif "task-graphlearning_run-05" in s.protocol_name:
            info[graphlearning_bold_run5].append(s.series_id)

    return info


# Any extra metadata that might not be automatically added by dcm2niix.

IntendedFor = {
    # task visit
    fmap_pa_task_run1: [ '{session}/func/sub-{subject}_{session}_task-flanker_bold.nii.gz' ],
    fmap_pa_task_run2: [ '{session}/func/sub-{subject}_{session}_task-graphlearning_run-01_bold.nii.gz',
                         '{session}/func/sub-{subject}_{session}_task-graphlearning_run-02_bold.nii.gz'],
    fmap_pa_task_run3: [ '{session}/func/sub-{subject}_{session}_task-graphlearning_run-03_bold.nii.gz',
                         '{session}/func/sub-{subject}_{session}_task-graphlearning_run-04_bold.nii.gz',
                         '{session}/func/sub-{subject}_{session}_task-graphlearning_run-05_bold.nii.gz'],
    }

