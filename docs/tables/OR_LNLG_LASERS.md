# OR_LNLG_LASERS

> This table contains the laser information for the surgical log (ORL).

**Overflow family:** [OR_LNLG_LASERS_2](OR_LNLG_LASERS_2.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 98  
**Org-specific columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LASER_DEVICE_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 3 | `LASER_TOTAL_WATTS` | NUMERIC |  | Total watts used for this laser device in this log. |
| 4 | `LASER_TOTAL_PULSES` | NUMERIC |  | The total pulses used for this laser device in this log. |
| 5 | `LASER_TYPE_C_NAME` | VARCHAR | org | The number populated in this column points to a particular laser type. |
| 6 | `LASER_LO_SET` | NUMERIC |  | The low setting for the laser. |
| 7 | `LASER_HI_SET` | NUMERIC |  | The high setting for the laser. |
| 8 | `LASER_MODE_C_NAME` | VARCHAR | org | The operation mode category number for this laser. |
| 9 | `LASER_PULSE_HI_FRE` | NUMERIC |  | The high pulse frequency of the laser. |
| 10 | `LASER_PULSE_LO_FRE` | NUMERIC |  | The low pulse frequency of the laser. |
| 11 | `LASER_FIBER_TYPE_C_NAME` | VARCHAR | org | The number populated in this column points to a particular fiber type used in this laser. |
| 12 | `LASER_TOT_JOULES` | NUMERIC |  | Stores the total joules used for the Laser. |
| 13 | `LASER_WAVELENGTH` | NUMERIC |  | Stores the wavelength of the Laser. |
| 14 | `LASER_TOTAL_TIME` | INTEGER |  | Stores the total time that the laser was used. |
| 15 | `LASER_FIBER_SIZE` | NUMERIC |  | The fiber size of the laser. |
| 16 | `LASER_PLUME_EXCV_C_NAME` | VARCHAR | org | The number populated in this column points to a particular evacuation method for plumes of smoke generated from laser cauterization. |
| 17 | `LASER_OPERATOR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `LASER_POWER_UNIT_C_NAME` | VARCHAR | org | The power unit category number for the power measurements documented on this laser. |
| 19 | `LASER_INTERVAL` | NUMERIC |  | The number of seconds for the interval of this laser. |
| 20 | `LASER_DURATION` | NUMERIC |  | The number of seconds for the duration of this laser. |
| 21 | `LASER_DELIV_METH_C_NAME` | VARCHAR | org | The delivery method category number for this laser. |
| 22 | `LASER_HANDPC_TYP_C_NAME` | VARCHAR | org | The number populated in this column points to the type of hand piece used for operating the laser. |
| 23 | `LASER_HANDPC_SIZE` | NUMERIC |  | The size in millimeters of the hand piece used while operating the laser device. |
| 24 | `LASER_MICRO_TYP_C_NAME` | VARCHAR | org | The number populated in this column points to the type of microscope used for operating the laser. |
| 25 | `LASER_MICRO_SIZE` | NUMERIC |  | The size (in millimeters) of the microscope used while operating the laser device. |
| 26 | `LASER_HEADPC_TYP_C_NAME` | VARCHAR | org | The number populated in this column points to the type of head piece used for operating the laser. |
| 27 | `LASER_HEADPC_SIZE` | NUMERIC |  | The size (in millimeters) of the head piece used while operating the laser device. |
| 28 | `LASER_FIBER_LOT_NUM` | VARCHAR |  | The lot number of the laser fiber. |
| 29 | `LASER_ENERGY_UNIT_C_NAME` | VARCHAR | org | The energy unit category number for the energy measurements documented on this laser. |
| 30 | `LSC_FIO2_LEVEL_OK_YN_NAME` | VARCHAR | org | The FiO2 level category number for the laser safety checklist. |
| 31 | `LSC_FIRE_EXTINGSR_C_NAME` | VARCHAR |  | The number populated in this column indicates whether a fire extinguisher was available: 11 - Yes , 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 32 | `LSC_FIRE_REDUCTN_YN_NAME` | VARCHAR | org | The fire risk reduction strategy category number for the laser safety checklist. |
| 33 | `LSC_FIRE_SAFE_DG_C_NAME` | VARCHAR |  | The number populated in this column indicates whether fire-retardant drapes and gowns were used: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 34 | `LSC_LSR_EVAC_POS_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the smoke evacuator was positioned during laser use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 35 | `LSC_ET_TUBE_USED_C_NAME` | VARCHAR |  | The number populated in this column indicates whether an endotracheal tube was used during laser use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 36 | `LSC_MOIST_ITEMS_C_NAME` | VARCHAR |  | The number populated in this column indicates whether moistened towels, gauze, and sponges were available for safety during laser use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 37 | `LSC_BASIN_WATER_C_NAME` | VARCHAR |  | The number populated in this column indicates whether a water-filled basin was available for safety during laser use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 38 | `LSC_PAT_EYE_PROT_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the patient's eyes were protected while the laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 39 | `LSC_STAFF_EYEWEAR_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the staff's eyes were protected while the laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 40 | `LSC_PHYS_EYEWEAR_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the physician's eyes were protected while the laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 41 | `LSC_EYEWEAR_AVAIL_C_NAME` | VARCHAR |  | The number populated in this column indicates whether protective eyewear was available: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 42 | `LSC_NO_EYEWEAR_RSN` | VARCHAR |  | The column displays the reason for the lack of protective eyewear documented by the circulating nurse. |
| 43 | `LSC_STAFF_MASK_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the staff used protective masks while the laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 44 | `LSC_MASK_AVAIL_C_NAME` | VARCHAR |  | The number populated in this column indicates whether protective masks were available: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 45 | `LSC_RCTL_PACK_RMV_C_NAME` | VARCHAR |  | The number populated in this column indicates whether rectal packing was removed: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 46 | `LSC_SIGNS_HUNG_C_NAME` | VARCHAR |  | The number populated in this column indicates whether appropriate danger signs were hung on doors: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 47 | `LSC_EYEWEAR_HUNG_C_NAME` | VARCHAR |  | The number populated in this column indicates whether protective eyewear was hung on doors available for use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 48 | `LSC_WINDOWS_COVRD_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the windows were covered while laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 49 | `LSC_STERILE_FLUID_C_NAME` | VARCHAR |  | The number populated in this column indicates whether sterile water and other sterile fluids were available: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 50 | `LSC_N2O_LEVEL_OK_YN_NAME` | VARCHAR | org | The N2O level category number for the laser safety checklist. |
| 51 | `LSC_DOOR_LOCKED_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the door was locked for safety while the laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 52 | `LSC_FIBER_CHECKED_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser fiber integrity was checked: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 53 | `LSC_FILTER_CABLE_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the microscope filter cable was positioned appropriately: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 54 | `LSC_MICROSCP_FLTR_C_NAME` | VARCHAR |  | The number populated in this column indicates whether there was a filter on the microscope: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 55 | `LSC_NON_REFLCTVTY_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the instruments were checked for non-reflectivity: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 56 | `LSC_LASER_TESTED_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser was test-fired prior to use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 57 | `LSC_KEY_RETURNED_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser key was returned: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 58 | `LSC_LASER_STANDBY_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser was in standby mode when not in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 59 | `LSC_PEDAL_POSITND_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser pedal position was appropriate: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 60 | `LSC_MICROSCP_CHKD_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the microscope was inspected prior to use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 61 | `LSC_SELF_CHECK_YN_NAME` | VARCHAR | org | The number populated in this column indicates whether the laser self-check was performed: 1 - Yes, 2 - No. |
| 62 | `LSC_BEAM_PATTERN_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser beam pattern was checked: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 63 | `LSC_FIBER_CALIB_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser fiber was calibrated: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 64 | `LSC_FIBER_EXPIRE_DT` | DATETIME |  | The column displays the expiration date of the fiber. |
| 65 | `LSC_FIBER_LOT_NUM` | VARCHAR |  | The column displays the lot number of the laser fiber. |
| 66 | `LSC_CIRCUIT_POS_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the circuit breaker was in the correct position: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 67 | `LSC_CORDS_PLUGGED_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the cords were plugged into appropriate outlets: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 68 | `LSC_DELIVERY_SYS_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the delivery system was properly connected: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 69 | `LSC_CORD_CONDTION_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the electrical cords were in good condition: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 70 | `LSC_LASER_REGION_C_NAME` | VARCHAR | org | The number populated in this column points to a particular operative region to which the laser was applied. |
| 71 | `LSC_GAS_ON_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser gas was turned on appropriately: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 72 | `LSC_GAS_OFF_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the laser gas was turned off appropriately: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 73 | `LSC_PE_EYE_PROT_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the patient was educated about laser eye protection: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 74 | `LSC_PE_MOVEMENT_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the patient was educated about not moving during the procedure: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 75 | `LSC_PE_TALKING_C_NAME` | VARCHAR |  | The number populated in this column indicates, for facial procedures, whether the patient was educated about not talking during the procedure: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 76 | `LSC_PE_NOISE_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the patient was educated about the noises that may occur during the procedure: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 77 | `LSC_PE_DRAPES_C_NAME` | VARCHAR |  | The number populated in this column indicates whether the patient was educated about the special drapings: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 78 | `LSC_ASST_AVAIL_C_NAME` | VARCHAR |  | The number populated in this column indicates whether a laser assistant was available while the laser was in use: 11 - Yes, 12 - No, 13 - Not Applicable (For older records, the column may return 0 for No, 1 for Yes, and 3 for Not Applicable). |
| 79 | `LASER_LATERALITY_C_NAME` | VARCHAR | org | This item stores laterality for a laser device. |
| 80 | `LSC_TIMEOUT_BEF_C_NAME` | VARCHAR |  | Documenting this item verifies that a timeout was done by all members of the surgical team prior to laser activation. |
| 81 | `LSC_EMERG_REVD_C_NAME` | VARCHAR |  | This item verifies that the laser emergency stop procedure was reviewed before use. |
| 82 | `LSC_PWR_SET_COMM_C_NAME` | VARCHAR |  | Documenting this item verifies that the laser power settings were communicated to the surgeon prior to its use. |
| 83 | `LSC_TIPS_RETURN_C_NAME` | VARCHAR |  | Document if laser tips were returned as part of laser checklist. |
| 84 | `LSC_CLN_AFTER_USE_C_NAME` | VARCHAR |  | The value populated in this column indicates whether a laser was cleaned after use in a procedure. |
| 85 | `LSC_STR_AFTER_USE_C_NAME` | VARCHAR |  | The value populated in this column indicates whether a laser was stored properly after use in a procedure. |
| 86 | `LASER_ENERGY_LOW` | NUMERIC |  | The initial/low energy setting for the laser in chosen units. |
| 87 | `LASER_ENERGY_HIGH` | NUMERIC |  | The final/high energy setting for the laser in chosen units. |
| 88 | `LASER_CPG_DENSITY` | NUMERIC |  | The density of the CPG laser. |
| 89 | `LASER_CPG_PATTERN` | NUMERIC |  | The pattern of the CPG laser. |
| 90 | `LASER_CPG_SIZE` | NUMERIC |  | The size of the CPG laser. |
| 91 | `LASER_DISTANCE` | NUMERIC |  | The distance between the laser fiber and the laser application point. This information is required for some vascular surgery research projects. |
| 92 | `LASER_LENGTH_TREATD` | NUMERIC |  | The length of the area treated by the laser. This information is required for some vascular surgery research projects. |
| 93 | `LASER_PULSE_DUR_LOW` | NUMERIC |  | Stores the low end of the pulse duration range for the laser. |
| 94 | `LASER_PULSE_DUR_HI` | NUMERIC |  | Stores the high end of the pulse duration range for the laser. |
| 95 | `LASER_AVG_POWER` | NUMERIC |  | This item is used to document laser average power. |
| 96 | `LASER_PULSE_FREQ_UNIT_C_NAME` | VARCHAR | org | The laser pulse frequency unit. |
| 97 | `LASER_ENERGY_PER_PULSE_UNIT_C_NAME` | VARCHAR | org | The laser energy per pulse unit. |
| 98 | `LASER_PULSE_DURATION_UNIT_C_NAME` | VARCHAR | org | The laser pulse duration unit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

