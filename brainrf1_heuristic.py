#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS"""
import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    last_run = len(seqinfo)

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

    # tms1 session
    nback_HiConHiLoWMgated_run1 = create_key(
        'sub-{subject}/{session}/func/sub-{subject}_{session}_task-nback_acq-HiConHiLoWMgated_run-01_bold')
    fmap_run1 = create_key(
        'sub-{subject}/{session}/fmap/sub-{subject}_{session}_run-01_phasediff')
    rest_gated = create_key(
        'sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_acq-gated_run-01_bold')
    nback_HiConHiLoWMgated_run2 = create_key(
        'sub-{subject}/{session}/func/sub-{subject}_{session}_task-nback_acq-HiConHiLoWMgated_run-02_bold')
    fmap_run2 = create_key(
        'sub-{subject}/{session}/fmap/sub-{subject}_{session}_run-02_phasediff')

    info = {
        t1w: [], t2w: [], hasc55_run1: [], hasc55_run2: [], hasc92: [], rand57: [],
        dwi_rpe: [], mean_perf: [], nback_HiConHiLoWMgated_run1: [], fmap_run1: [],
        nback_HiConHiLoWMgated_run2: [],
    }

    for s in seqinfo:
        protocol = s.protocol_name.lower()
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

    return info


IntendedFor = {
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_epi': [
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-01_dwi',
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC55_run-02_dwi',
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-HASC92_dwi',
        'sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-RAND57_dwi']
}
