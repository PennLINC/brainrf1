#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS with LoConHiLo stimulation condition visits"""
import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


# Baseline session
t1w = create_key(
    'sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
t2w = create_key(
    'sub-{subject}/{session}/anat/sub-{subject}_{session}_T2w')

# CS-DSI scans
hasc55_run1 = create_key(
    'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-01_dwi')
hasc55_run2 = create_key(
    'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-02_dwi')
hasc92 = create_key(
    'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC92_dwi')
rand57 = create_key(
    'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-RAND57_dwi')
dwi_rpe = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_epi')

# ASL Scans
mean_perf = create_key(
    'sub-{subject}/{session}/asl/sub-{subject}_{session}_CBF')
raw_asl = create_key(
    'sub-{subject}/{session}/asl/sub-{subject}_{session}_asl')
m0 = create_key(
    'sub-{subject}/{session}/asl/sub-{subject}_{session}_MZeroScan')

# QSM scans
qsm_mag = create_key(
    'sub-{subject}/{session}/qsm/sub-{subject}_{session}_magnitude{item}')
qsm_ph = create_key(
    'sub-{subject}/{session}/qsm/sub-{subject}_{session}_phase{item}')
    
# **********************************************************************************
# tms session

# conditions (run 1)
nback_LoConHiLoWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-LoConHiLoWMgated_run-01_bold')    
 
# conditions (run 2)   
nback_LoConHiLoWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-LoConHiLoWMgated_run-02_bold')   

# iTBS
rest_gated = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}'
    '_task-rest_acq-gated_bold')

# field map         
fmap_pa_tms_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-01_epi')
fmap_ap_tms_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-01_epi')
    
fmap_pa_tms_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-02_epi')
fmap_ap_tms_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-02_epi')    

# **********************************************************************************
# task session

# field maps
fmap_pa_task_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-01_epi')
fmap_ap_task_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-01_epi')

fmap_pa_task_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-02_epi')
fmap_ap_task_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-02_epi')

fmap_pa_task_run3 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-03_epi')
fmap_ap_task_run3 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-03_epi')

fmap_pa_task_run4 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-04_epi')
fmap_ap_task_run4 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-04_epi')

fmap_pa_task_run5 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-05_epi')
fmap_ap_task_run5 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-05_epi')

fmap_pa_task_run6 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-06_epi')
fmap_ap_task_run6 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-06_epi')


# flanker
flanker_bold = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-flanker_bold')
flanker_pmu = create_key( # might remove later 
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-flanker_bold_PMU')
    
# graph learning
graphlearning_bold_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-01_bold')
graphlearning_pmu_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-01_bold_PMU')

graphlearning_bold_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-02_bold')
graphlearning_pmu_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-02_bold_PMU')
    
graphlearning_bold_run3 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-03_bold')
graphlearning_pmu_run3 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-03_bold_PMU')
    
graphlearning_bold_run4 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-04_bold')
graphlearning_pmu_run4 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-04_bold_PMU')

graphlearning_bold_run5 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-05_bold')
graphlearning_pmu_run5 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-05_bold_PMU')

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
        # baseline
        t1w: [], t2w: [], hasc55_run1: [], hasc55_run2: [], hasc92: [], rand57: [],
        dwi_rpe: [], mean_perf: [], qsm_ph: [], qsm_mag: [],

        # TMS scans
        nback_LoConHiLoWMgated_run1: [],
        rest_gated: [],
        nback_LoConHiLoWMgated_run2: [],
        
        fmap_pa_tms_run1: [], fmap_ap_tms_run1: [],
        fmap_pa_tms_run2: [], fmap_ap_tms_run2: [],
        
        # task
        fmap_pa_task_run1: [], fmap_ap_task_run1: [],
        fmap_pa_task_run2: [], fmap_ap_task_run2: [],
        fmap_pa_task_run3: [], fmap_ap_task_run3: [],
        fmap_pa_task_run4: [], fmap_ap_task_run4: [],
        fmap_pa_task_run5: [], fmap_ap_task_run5: [],
        fmap_pa_task_run6: [], fmap_ap_task_run6: [],
        
        flanker_bold: [], flanker_pmu: [],
        graphlearning_bold_run1: [], graphlearning_pmu_run1: [],
        graphlearning_bold_run2: [], graphlearning_pmu_run2: [],
        graphlearning_bold_run3: [], graphlearning_pmu_run3: [],
        graphlearning_bold_run4: [], graphlearning_pmu_run4: [],
        graphlearning_bold_run5: [], graphlearning_pmu_run5: [],
    }
    
    for s in seqinfo:
        protocol = s.protocol_name.lower()

        # Baseline Anatomicals
        if "anat_t1w" in protocol:
            info[t1w].append(s.series_id)
        elif "anat_t2w" in protocol:
            info[t2w].append(s.series_id)
        elif "acq-hasc55_run-02" in protocol:
            info[hasc55_run2].append(s.series_id)
        elif "acq-hasc55_run-01" in protocol:
            info[hasc55_run1].append(s.series_id)
        elif "acq-hasc92" in protocol:
            info[hasc92].append(s.series_id)
        elif "acq-rand57" in protocol:
            info[rand57].append(s.series_id)
        elif "fmap_acq-dmridistmap" in protocol:
            info[dwi_rpe].append(s.series_id)
        elif protocol.startswith('qsm'):
            if "P" in s.image_type:
                info[qsm_ph].append(s.series_id)
            elif "M" in s.image_type:
                info[qsm_mag].append(s.series_id)

        # TMS day  
        elif "acq-fMRIdistmap_dir-PA_run-01" in s.protocol_name:
            info[fmap_pa_tms_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-01" in s.protocol_name:
            info[fmap_ap_tms_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-02" in s.protocol_name:
            info[fmap_pa_tms_run2].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-02" in s.protocol_name:
            info[fmap_ap_tms_run2].append(s.series_id)
        
        elif "task-nback_acq-LoConHiLoWMgated_run-01" in s.protocol_name:
            info[nback_LoConHiLoWMgated_run1].append(s.series_id)
        
        elif "task-nback_acq-LoConHiLoWMgated_run-02" in s.protocol_name:
            info[nback_LoConHiLoWMgated_run2].append(s.series_id)
        
        # Task day
        elif "acq-fMRIdistmap_dir-PA_run-01" in s.protocol_name:
            info[fmap_pa_task_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-01" in s.protocol_name:
            info[fmap_ap_task_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-02" in s.protocol_name:
            info[fmap_pa_task_run2].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-02" in s.protocol_name:
            info[fmap_ap_task_run2].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-03" in s.protocol_name:
            info[fmap_pa_task_run3].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-03" in s.protocol_name:
            info[fmap_ap_task_run3].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-04" in s.protocol_name:
            info[fmap_pa_task_run4].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-04" in s.protocol_name:
            info[fmap_ap_task_run4].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-05" in s.protocol_name:
            info[fmap_pa_task_run5].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-05" in s.protocol_name:
            info[fmap_ap_task_run5].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-06" in s.protocol_name:
            info[fmap_pa_task_run6].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-06" in s.protocol_name:
            info[fmap_ap_task_run6].append(s.series_id)
        
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


# Any extra metadata that might not be automatically added by dcm2niix. H

IntendedFor = {
    # baseline
    dwi_rpe: [
        '{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-01_dwi.nii.gz',
        '{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-02_dwi.nii.gz',
        '{session}/dwi/sub-{subject}_{session}_acq-HASC92_dwi.nii.gz',
        '{session}/dwi/sub-{subject}_{session}_acq-RAND57_dwi.nii.gz'],

    m0: [ '{session}/asl/sub-{subject}_{session}_asl.nii.gz' ],
    
    #   **** sub-C412-specific ****
    # tms visits
    # LoConHiLo    
    fmap_pa_tms_run1: [ '{session}/func/sub-{subject}_{session}_task-nback_acq-LoConHiLoWMgated_run-01_bold.nii.gz',
                     '{session}/func/sub-{subject}_{session}_task-rest_acq-gated_bold.nii.gz'],
    fmap_ap_tms_run1: [ '{session}/func/sub-{subject}_{session}_task-nback_acq-LoConHiLoWMgated_run-01_bold.nii.gz',
                    '{session}/func/sub-{subject}_{session}_task-rest_acq-gated_bold.nii.gz'],
    fmap_pa_tms_run2:[ '{session}/func/sub-{subject}_{session}_task-nback_acq-LoConHiLoWMgated_run-02_bold.nii.gz'],
    fmap_ap_tms_run2:[ '{session}/func/sub-{subject}_{session}_task-nback_acq-LoConHiLoWMgated_run-02_bold.nii.gz'],
    }
'''''
    # task visit
    fmap_pa_task_run1: [ '{session}/func/sub-{subject}_{session}_task-flanker_bold.nii.gz' ],
    fmap_ap_task_run1: [ '{session}/func/sub-{subject}_{session}_task-flanker_bold.nii.gz' ],
    fmap_pa_task_run2: [ '{session}/func/sub-{subject}_{session}_task-graphlearning_run-01_bold.nii.gz' ],
    fmap_ap_task_run2: [ '{session}/func/sub-{subject}_{session}_task-graphlearning_run-01_bold.nii.gz' ],
    fmap_pa_task_run3: [ '{session}/func/sub-{subject}_{session}_task-graphlearning_run-02_bold.nii.gz' ],
    fmap_ap_task_run3: [ '{session}/func/sub-{subject}_{session}_task-graphlearning_run-02_bold.nii.gz' ],
'''
    
