#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS for subject C412"""
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
nback_HiConHiLoWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated_run-01_bold')
nback_LoConHiLoWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-LoConHiLoWMgated_run-01_bold')
nback_HiConLoHiWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConLoHiWMgated_run-01_bold')
nback_LoConLoHiWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-LoConLoHiWMgated_run-01_bold')    
 
# conditions (run 2)   
nback_HiConHiLoWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated_run-02_bold')
nback_LoConHiLoWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-LoConHiLoWMgated_run-02_bold')
nback_HiConLoHiWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConLoHiWMgated_run-02_bold')
nback_LoConLoHiWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-LoConLoHiWMgated_run-02_bold')   

# iTBS
rest_gated = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}'
    '_task-rest_acq-gated_bold')

# field map          
fmap_run1_ph = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_run-01_phasediff')
fmap_run1_mag = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_run-01_magnitude{item}')
fmap_run2_ph = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_run-02_phasediff')
fmap_run2_mag = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_run-02_magnitude{item}')

# **********************************************************************************
# task session

# field maps
fmap_pa_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-01_epi')
fmap_ap_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-01_epi')

fmap_pa_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-02_epi')
fmap_ap_run2 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-02_epi')

fmap_pa_run3 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-03_epi')
fmap_ap_run3 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-03_epi')

fmap_pa_run4 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-04_epi')
fmap_ap_run4 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-04_epi')

fmap_pa_run5 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-05_epi')
fmap_ap_run5 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-AP_run-05_epi')

fmap_pa_run6 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_run-06_epi')
fmap_ap_run6 = create_key(
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
        nback_HiConHiLoWMgated_run1: [],
        nback_LoConHiLoWMgated_run1: [],
        nback_HiConLoHiWMgated_run1: [],
        nback_LoConLoHiWMgated_run1: [],
        rest_gated: [],
        nback_HiConHiLoWMgated_run2: [],
        nback_LoConHiLoWMgated_run2: [],
        nback_HiConLoHiWMgated_run2: [],
        nback_LoConLoHiWMgated_run2: [],
        fmap_run1_ph: [], fmap_run1_mag: [],
        fmap_run2_ph: [], fmap_run2_mag: [],

        
        # task
        fmap_pa_run1: [], fmap_ap_run1: [],
        fmap_pa_run2: [], fmap_ap_run2: [],
        fmap_pa_run3: [], fmap_ap_run3: [],
        fmap_pa_run4: [], fmap_ap_run4: [],
        fmap_pa_run5: [], fmap_ap_run5: [],
        fmap_pa_run6: [], fmap_ap_run6: [],
        
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
        elif "task-nback_acq-HiConHiLoWMgated_run-01" in s.protocol_name:
            info[nback_HiConHiLoWMgated_run1].append(s.series_id)
        elif "task-nback_acq-LoConHiLoWMgated_run-01" in s.protocol_name:
            info[nback_LoConHiLoWMgated_run1].append(s.series_id)
        elif "task-nback_acq-HiConLoHiWMgated_run-01" in s.protocol_name:
            info[nback_HiConLoHiWMgated_run1].append(s.series_id)
        elif "task-nback_acq-LoConLoHiWMgated_run-01" in s.protocol_name:
            info[nback_LoConLoHiWMgated_run1].append(s.series_id)
        
        # fmaps for subject C412
        elif "fmap_run-01" in protocol and "M" in s.image_type:
            info[fmap_run1_mag].append(s.series_id)
        elif "fmap_run-01" in protocol and "P" in s.image_type:
            info[fmap_run1_ph].append(s.series_id)
        
        elif "task-rest_acq-gated_bold" in s.protocol_name:
            info[rest_gated].append(s.series_id)    
            
        elif "fmap_run-02" in protocol and "M" in s.image_type:
            info[fmap_run2_mag].append(s.series_id)
        elif "fmap_run-02" in protocol and "P" in s.image_type:
            info[fmap_run2_ph].append(s.series_id)
            
        elif "task-nback_acq-HiConHiLoWMgated_run-02" in s.protocol_name:
            info[nback_HiConHiLoWMgated_run2].append(s.series_id)
        elif "task-nback_acq-LoConHiLoWMgated_run-02" in s.protocol_name:
            info[nback_LoConHiLoWMgated_run2].append(s.series_id)
        elif "task-nback_acq-HiConLoHiWMgated_run-02" in s.protocol_name:
            info[nback_HiConLoHiWMgated_run2].append(s.series_id)
        elif "task-nback_acq-LoConLoHiWMgated_run-02" in s.protocol_name:
            info[nback_LoConLoHiWMgated_run2].append(s.series_id)
        
        # Task day
        # **** for subject C412 only ****
        elif "acq-fMRIdistmap_dir-PA_run-01" in s.protocol_name:
            info[fmap_pa_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-01" in s.protocol_name:
            info[fmap_ap_run1].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-02" in s.protocol_name:
            info[fmap_pa_run2].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-02" in s.protocol_name:
            info[fmap_ap_run2].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-03" in s.protocol_name:
            info[fmap_pa_run3].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-03" in s.protocol_name:
            info[fmap_ap_run3].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-04" in s.protocol_name:
            info[fmap_pa_run4].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-04" in s.protocol_name:
            info[fmap_ap_run4].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-05" in s.protocol_name:
            info[fmap_pa_run5].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-05" in s.protocol_name:
            info[fmap_ap_run5].append(s.series_id)
        elif "acq-fMRIdistmap_dir-PA_run-06" in s.protocol_name:
            info[fmap_pa_run6].append(s.series_id)
        elif "acq-fMRIdistmap_dir-AP_run-06" in s.protocol_name:
            info[fmap_ap_run6].append(s.series_id)
        
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
MetadataExtras = {
    fmap_run1_ph: {
        "EchoTime1": 0.004,
        "EchoTime2": 0.006
    },
    
    fmap_run2_ph: {
        "EchoTime1": 0.004,
        "EchoTime2": 0.006
    }
}


IntendedFor = {
    # baseline
    dwi_rpe: [
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-01_dwi.nii.gz',
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-02_dwi.nii.gz',
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC92_dwi.nii.gz',
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-RAND57_dwi.nii.gz'],

    m0: [ 'sub-{subject}/{session}/asl/sub-{subject}_{session}_asl.nii.gz' ],
    
    #   **** sub-C412-specific ****
    # tms visits
    fmap_run1_ph: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-nback_acq-HiConHiLoWMgated_run-01_bold.nii.gz',
                    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_acq-gated_bold.nii.gz'],
    fmap_run1_mag:[ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-nback_acq-HiConHiLoWMgated_run-01_bold.nii.gz',
                    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_acq-gated_bold.nii.gz'],
    fmap_run2_ph: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-nback_acq-HiConHiLoWMgated_run-02_bold.nii.gz'],
    fmap_run2_mag:[ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-nback_acq-HiConHiLoWMgated_run-02_bold.nii.gz'], 
    
    # task visit
    fmap_pa_run1: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-flanker_bold.nii.gz' ],
    fmap_ap_run1: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-flanker_bold.nii.gz' ],
    fmap_pa_run2: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-01.nii.gz' ],
    fmap_ap_run2: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-01.nii.gz' ],
    fmap_pa_run3: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-02.nii.gz' ],
    fmap_ap_run3: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-02.nii.gz' ],
    fmap_pa_run4: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-03.nii.gz' ],
    fmap_ap_run4: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-03.nii.gz' ],
    fmap_pa_run5: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-04.nii.gz' ],
    fmap_ap_run5: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-04.nii.gz' ],
    fmap_pa_run6: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-05.nii.gz' ],
    fmap_ap_run6: [ 'sub-{subject}/{session}/func/sub-{subject}_{session}_task-graphlearning_run-05.nii.gz' ],
}
