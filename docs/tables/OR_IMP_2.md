# OR_IMP_2

> The OR_IMP_2 table contains implant information specific to Mechanical Circulatory System and Implantable Cardioverter Defibrillator devices.

**Overflow of:** [OR_IMP](OR_IMP.md)  
**Primary key:** `IMPLANT_ID`  
**Columns:** 98  
**Org-specific columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `PRIMARY_DEVICE_YN` | VARCHAR |  | Specifies whether this is the patient's primary device. |
| 3 | `DEVICE_EXPLANT_REASON_C_NAME` | VARCHAR | org | The category ID for the reason a device was explanted. |
| 4 | `CONSOLE_TRACKING_NUM` | VARCHAR |  | The mechanical circulatory system device console tracking number. |
| 5 | `CANNULAE_LOC_INFLOW_C_NAME` | VARCHAR | org | The category ID for a device's cannulae inflow location. |
| 6 | `CANNULAE_LOC_OUTFLOW_C_NAME` | VARCHAR | org | The category ID for a device's cannulae outflow location. |
| 7 | `DEVICE_STUDY_NUM` | VARCHAR |  | The device research study number. |
| 8 | `DEVICE_STRAT_TIME_IMP_C_NAME` | VARCHAR | org | The category ID for the intended treatment of an implanted mechanical circulatory device. |
| 9 | `DEVICE_STRAT_TIME_IMP_FREETEXT` | VARCHAR |  | The intended treatment for an implanted mechanical circulatory device. This is a free-text field for describing values not found in Device Strategy At Time of Implant (I IMP 16507). |
| 10 | `ICD_CS_LV_SUCCESS_C_NAME` | VARCHAR |  | Indicates if the coronary sinus/left ventricular (CS/LV) lead was successfully implanted. This item corresponds to ICD Sequence 6145. |
| 11 | `ICD_CSLV_NT_IMP_C_NAME` | VARCHAR |  | Indicates the reason a Coronary Sinus Access or Left Ventricular (CS/LV) lead was not implanted. |
| 12 | `ICD_LET_SUCCESSFUL` | INTEGER |  | Indicates the lowest energy tested (LET) or defibrillation threshold that demonstrated that the device performs successfully (in joules). |
| 13 | `ICD_LET_NOT_TSTD_YN` | VARCHAR |  | Indicates the lowest energy tested (LET) that was successful was not tested. |
| 14 | `ICD_ULV` | INTEGER |  | Indicates the upper limit of vulnerability (ULV) in joules. |
| 15 | `ICD_ULV_NOT_TEST_YN` | VARCHAR |  | Indicates the upper limit of vulnerability (ULV) was not tested. |
| 16 | `ICD_REIMP_ENDBAT_YN` | VARCHAR |  | Indicates if a reason for reimplant is the end of expected battery life of a previous ICD. |
| 17 | `ICD_REIMP_LEADRVN_YN` | VARCHAR |  | Indicates if a reason for reimplant is that the generator is being replaced at the time of lead revision. |
| 18 | `ICD_REIMP_UPGRADE_YN` | VARCHAR |  | Indicates if a reason for reimplant is an upgrade of a previous device with additional pacing capabilities such as an upgrade from a single to a dual chamber device, or the replacement of a non-CRT with a CRT device. |
| 19 | `ICD_REIMP_INFECTN_YN` | VARCHAR |  | Indicates if a reason for reimplant is due to infection in the location of the previously implanted device. |
| 20 | `ICD_REIMP_MNRCALL_YN` | VARCHAR |  | Indicates if a reason for reimplant is that the previous device has been recognized by the manufacturer as demonstrating a recurring performance failure resulting in an advisory letter to physicians. This may or may not reach the level of a food and drug administration (FDA) designated recall. This also may or may not have led to device malfunction. |
| 21 | `ICD_REIMP_FLTYHDR_YN` | VARCHAR |  | Indicates if a reason for reimplant is that there was a faulty connector/header which required Coding Instructions: another implant. |
| 22 | `ICD_REIMP_DVRELOC_YN` | VARCHAR |  | Indicates if a reason for reimplant is that the device needed to be relocated because of a medical condition, or procedure near the original pocket. An example is if the patient was diagnosed with breast cancer and required treatment or surgery near the original implant. |
| 23 | `ICD_REIMP_MALFUNC_YN` | VARCHAR |  | Indicates if a reason for reimplant is that the previous generator has malfunctioned. The device performance is outside the manufacturer's designated specification and cannot be resolved with reprogramming, necessitating in the replacement of the device, in the opinion of the physician. |
| 24 | `ICD_MLFN_RSN_C_NAME` | VARCHAR |  | Indicates the reason for malfunction of the ICD implant. |
| 25 | `ICD_ATPSHCK_DLVRD_YN` | VARCHAR |  | Indicates if, at any point in time, the ICD being removed had delivered antitachycardia pacing (ATP) or shock therapy. |
| 26 | `ICD_ATPSHCK_APPRO_YN` | VARCHAR |  | Indicates if, at any point in time, the Implantable Cardioverter Defibrillator (ICD) being removed had delivered appropriate antitachycardia pacing (ATP) or shock therapy for spontaneous ventricular tachycardia and/or ventricular fibrillation. |
| 27 | `ICD_ATP_SUCCESSFL_YN` | VARCHAR |  | Indicates if the antitachycardia pacing (ATP) therapy for ventricular tachycardia and/or ventricular fibrillation was successful. |
| 28 | `ICD_SHCK_SUCCESS_YN` | VARCHAR |  | Indicates if the shock therapy for ventricular tachycardia and/or ventricular fibrillation was successful. |
| 29 | `ICD_LD_PLCMNT_ISS_YN` | VARCHAR |  | Indicates if the existing lead had any placement issues. |
| 30 | `ICD_LD_PERF_YN` | VARCHAR |  | Indicates if there was penetration of the existing lead through a systemic vein, coronary vein, or the myocardium. |
| 31 | `ICD_PT_CLIN_STATS_YN` | VARCHAR |  | Indicates if a non-lead related medical or surgical procedure required the existing lead to be replaced. |
| 32 | `ICD_LD_DISLDGEMNT_YN` | VARCHAR |  | Indicates if there was movement (macroscopic or microscopic) of an existing lead within the heart or vascular tree away from the original implantation site. |
| 33 | `ICD_LEAD_INFCTION_YN` | VARCHAR |  | Indicates if there was a suspected or documented infection of the existing lead. |
| 34 | `ICD_EROSION_YN` | VARCHAR |  | Indicates if there was erosion of the existing lead. |
| 35 | `ICD_FAULTY_CONNCT_YN` | VARCHAR |  | Indicates if there was a faulty connector/header in the existing lead. |
| 36 | `ICD_DOC_INFECTION_YN` | VARCHAR |  | Indicates if there was a documented infection of the existing lead as evidenced by positive microbiological cultures/smears or other microbiological evidence indicating infection. |
| 37 | `ICD_PACING_ISSUE_YN` | VARCHAR |  | Indicates if there were pacing issues such as oversensing, undersensing, failure to pace, failure to capture with acceptable safety margin, or extracardiac stimulation. |
| 38 | `ICD_OVERSENSE_YN` | VARCHAR |  | Indicates if the existing lead was functioning abnormally due to oversensing. Oversensing manifests as sensing of electrical signals not related to cardiac depolarization of the lead chamber that cannot be resolved acceptably by device reprogramming. |
| 39 | `ICD_UNDERSENSE_YN` | VARCHAR |  | Indicates if the existing lead was functioning abnormally due to undersensing. Undersensing manifests as failure to sense appropriate cardiac depolarizations that cannot be resolved with reprogramming. |
| 40 | `ICD_FAIL_TO_PACE_YN` | VARCHAR |  | Indicates if the existing lead was functioning abnormally because there was failure to pace. Failure to pace manifests as absence of pacemaker stimulation artifacts on electrocardiographic recordings despite rates below pacemaker programmed rate. |
| 41 | `ICD_FAIL_SF_MRGN_YN` | VARCHAR |  | Indicates if the existing lead was functioning abnormally because there was failure to capture with acceptable safety margins. This manifests as a high pacing threshold that results in either intermittent failure to capture at maximal programmed output or excessive batter drain leading to premature battery exhaustion. |
| 42 | `ICD_XTRACARD_STIM_YN` | VARCHAR |  | Indicates if the existing lead was functioning abnormally because there was extracardiac stimulation. This manifests as stimulation by the lead of non-cardiac structures such as the diaphragm, chest wall, or pectoral muscle. |
| 43 | `ICD_DEFIB_ISSUES_YN` | VARCHAR |  | Indicates if the existing lead had defibrillation issues such as oversensing with or without shock/ATP, or failed shocks/inadequate Defibrillation Threshold (DFT) safety margins. |
| 44 | `ICD_DFIB_OVRSNS_W_YN` | VARCHAR |  | Indicates if the existing lead had defibrillation problems due to oversensing with shock/antitachycardia pacing (ATP). This manifests as sensing of non-cardiac depolarization signals that met arrhythmia detection criteria and elicited programmed tachyarrhythmia therapy. |
| 45 | `ICD_DFB_OVRSNS_WO_YN` | VARCHAR |  | Indicates if the existing lead had defibrillation issues due to oversensing without shock/antitachycardia pacing (ATP). This manifests as sensing of non-cardiac depolarization signals that did not meet arrhythmia detection criteria and do not elicit programmed tachyarrhythmia therapy. |
| 46 | `ICD_DFB_FAIL_SHCK_YN` | VARCHAR |  | Indicates if the existing lead had defibrillation issues due to failed shocks or inadequate defibrillation threshold safety margins. |
| 47 | `ICD_LD_INTG_ISSUE_YN` | VARCHAR |  | Indicates if the existing lead had abnormal function due to lead integrity issues. |
| 48 | `ICD_LD_CNDCT_FAIL_YN` | VARCHAR |  | Indicates if the existing lead had abnormal function due to a lead integrity issue of conductor failure. Conductor failure manifests by high lead impedance either absolutely (above manufacturer's product specifications) or by a significant increase from previously stable chronic values. |
| 49 | `ICD_LD_INSUL_FAIL_YN` | VARCHAR |  | Indicates if the existing lead had abnormal function due to a lead integrity issue of insulation failure. Insulation failure manifests as low lead impedance either absolutely (below manufacture's product specifications) or by a significant decrease from previously stable chronic values. |
| 50 | `IMPLANTATION_TEMP_C_NAME` | VARCHAR | org | This item stores the tissue temperature at implantation. |
| 51 | `STORAGE_TEMP_C_NAME` | VARCHAR | org | This item stores the tissue storage temperature. |
| 52 | `IMPLANT_CLASS_C_NAME` | VARCHAR | org | Stores the class of the implant. |
| 53 | `PATIENT_REQUESTED_C_NAME` | VARCHAR | org | Stores if the implant was requested by the patient. |
| 54 | `IMPLANT_FIN_COMMENT` | VARCHAR |  | Stores the comment for the implant. |
| 55 | `CLINICAL_IND_C_NAME` | VARCHAR | org | Stores the clinical indication for the requested implant. |
| 56 | `GUDID_REQUEST_C_NAME` | VARCHAR |  | This column stores the status of a request to the FDA's GUDID for information on this implant. |
| 57 | `GUDID_BRAND_NAME` | VARCHAR |  | This column stores the brand name obtained from Global Unique Device Identification Database (GUDID) for an implant. |
| 58 | `GUDID_VERSION_NUM` | VARCHAR |  | This column stores the version or model number obtained from GUDID for an implant. |
| 59 | `GUDID_COMPANY_NAME` | VARCHAR |  | This column stores the company name obtained from GUDID for an implant. |
| 60 | `GUDID_CONTAINS_LATEX_RUBBER` | VARCHAR |  | This column stores whether or not an implant is labeled as containing natural rubber latex or dry natural rubber according to GUDID. GUDID returns either a "true" or a "false" for this item. However, this is not a YN column as we want to be able to handle any new values that might be added for this field. |
| 61 | `GUDID_IMPLANT_DESCRIPTION` | VARCHAR |  | This column stores the implant Global Medical Device Nomenclature (GMDN) Preferred Term name obtained from GUDID for an implant. |
| 62 | `TISSUE_IDNT_CODE` | VARCHAR |  | This column stores the Distinct Identification Code for tissue implants. |
| 63 | `TISSUE_DIC_FLAGS` | VARCHAR |  | This column stores flag characters associated with the distinct identification code of a tissue implant. |
| 64 | `CONTAINER_LOT_NUMBER` | VARCHAR |  | This stores the container lot number for implants. |
| 65 | `CONTAINER_EXP_DATE` | DATETIME |  | This stores the container expiration date for implants. |
| 66 | `TISSUE_PLACED_IN_STORAGE_DTTM` | DATETIME (UTC) |  | This stores the instant the tissue was placed in storage. |
| 67 | `TISSUE_PLACED_IN_STORAGE_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 68 | `TISSUE_DONATION_VERIFIED_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 69 | `TISSUE_CULTURE_COLLECTED_BY_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 70 | `TISSUE_CULTURE_SENT_BY_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 71 | `TISSUE_REMOVED_FROM_STORAGE_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 72 | `TISSUE_REC_STORAGE_TEMPERATURE` | NUMERIC |  | This stores information regarding the recommended storage temperature. |
| 73 | `IMPLANT_APPROACH_C_NAME` | VARCHAR | org | The category ID for the approach taken for the implant/joint. |
| 74 | `FEMUR_MANUFACTURER_C_NAME` | VARCHAR | org | The femur manufacturer category ID for the implant. |
| 75 | `TIBIA_MANUFACTURER_C_NAME` | VARCHAR |  | The tibia manufacturer category ID for the implant. |
| 76 | `PREV_FEMUR_MANUFACTURER_C_NAME` | VARCHAR |  | The old femur prosthesis manufacturer category ID for the implant. |
| 77 | `PREV_TIBIA_MANUFACTURER_C_NAME` | VARCHAR |  | The old tibia prosthesis manufacturer category ID for the implant. |
| 78 | `CEMENT_USED_YN` | VARCHAR |  | Indicates whether cement was used for this implant. Y indicates cement was used. N indicates cement was not used. Null indicates cement usage was not assessed or is not applicable for this type of implant. |
| 79 | `CEMENT_USED_FEMUR_YN` | VARCHAR |  | Indicates whether cement was used on the femur for this implant. Y indicates cement was used on the femur. N indicates cement was not used on the femur. Null indicates cement usage was not assessed or is not applicable for this type of implant. |
| 80 | `CEMENT_USED_ACETABULUM_YN` | VARCHAR |  | Indicates whether cement was used on the acetabulum for this implant. Y indicates cement was used on the acetabulum. N indicates cement was not used on the acetabulum. Null indicates cement usage was not assessed or is not applicable for this type of implant. |
| 81 | `CEMENT_USED_TIBIA_YN` | VARCHAR |  | Indicates whether cement was used on the tibia for this implant. Y indicates cement was used on the tibia. N indicates cement was not used on the tibia. Null indicates cement usage was not assessed or is not applicable for this type of implant. |
| 82 | `CEMENT_USED_PATELLA_YN` | VARCHAR |  | Indicates whether cement was used on the patella for this implant. Y indicates cement was used on the patella. N indicates cement was not used on the patella. Null indicates cement usage was not assessed or is not applicable for this type of implant. |
| 83 | `CEMENT_USED_OTHER_YN` | VARCHAR |  | Indicates whether cement was used on another prosthesis for this implant. Y indicates cement was used on another prosthesis. N indicates cement was not used on another prosthesis. Null indicates cement usage was not assessed or is not applicable for this type of implant. |
| 84 | `CEMENT_TECHNIQUE_C_NAME` | VARCHAR | org | The cement application technique category ID for the implant. |
| 85 | `CEMENT_MIX_C_NAME` | VARCHAR | org | The cement mix category ID for the implant. |
| 86 | `CEMENT_MANUFACTURER_C_NAME` | VARCHAR |  | The cement manufacturer category ID for the implant. |
| 87 | `BONE_GRAFT_C_NAME` | VARCHAR | org | The bone graft type category ID for the implant. |
| 88 | `DEGEN_GLENOHUMERAL_C_NAME` | VARCHAR | org | The glenohumeral joint degeneration category ID for the implant. This describes the type of degeneration exhibited by the joint. |
| 89 | `AP_CONGRUENCE_C_NAME` | VARCHAR | org | The anteroposterior congruence category ID for the implant. This describes the congruence of the joint in the anteroposterior direction. |
| 90 | `CENTRIC_JOINT_C_NAME` | VARCHAR | org | The centric joint type category ID for the implant. |
| 91 | `POST_ECCENTRIC_CAPUT_C_NAME` | VARCHAR | org | The posteriorly eccentric caput category ID for the implant. |
| 92 | `ANT_ECCENTRIC_CAPUT_C_NAME` | VARCHAR | org | The anteriorly eccentric caput category ID for the implant. |
| 93 | `CRANIO_CONGRUENCE_C_NAME` | VARCHAR | org | The craniocaudal congruence category ID for the implant. This describes the congruence of the joint in the craniocaudal direction. |
| 94 | `SUP_ECCENTRIC_CAPUT_C_NAME` | VARCHAR | org | The superiorly eccentric caput category ID for the implant. |
| 95 | `JOINT_CONGRUENCE_C_NAME` | VARCHAR | org | The joint congruence category ID for the implant. |
| 96 | `GLENOID_COMPONENT_C_NAME` | VARCHAR | org | The glenoid component category ID for the implant. |
| 97 | `HUMERAL_COMPONENT_C_NAME` | VARCHAR | org | The humeral component category ID for the implant. |
| 98 | `CONTAINER_EXPIRATION_TIME` | DATETIME (Local) |  | This stores the container expiration time for implants. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

