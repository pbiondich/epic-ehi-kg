# HSC_SPEC_INFO

> This table holds the specimen details.

**Primary key:** `RECORD_ID`  
**Columns:** 81  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | This column holds the specimen record ID. |
| 2 | `RECORD_NAME` | VARCHAR |  | This column holds the system generated name for the specimen record. |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...). |
| 4 | `SPECIMEN_TYPE_C_NAME` | VARCHAR | org | This column is used to store type of specimen. |
| 5 | `SPECIMEN_DESC` | VARCHAR |  | This column stores a short description about the specimen that is being collected. |
| 6 | `SPECIMEN_SOURCE_C_NAME` | VARCHAR | org | This column is used to store source from where specimen is collected. |
| 7 | `SPECIMEN_ID` | VARCHAR | shared | This column is used to store unique ID for the specimen. |
| 8 | `COLL_BY_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `COLL_DATE` | DATETIME |  | This column is used to store collection date for specimen. |
| 10 | `COLL_TIME` | DATETIME (Local) |  | This column is used to store collection time for specimen. |
| 11 | `DEST_C_NAME` | VARCHAR | org | This column is used to store destination where specimen was sent. |
| 12 | `TRANSPORTED_BY_ID` | VARCHAR |  | A free-text description of the method that transported the specimen. |
| 13 | `PRIORITY_C_NAME` | VARCHAR | org | This column stores the priority of the specimen when it is sent to the lab. |
| 14 | `SENT_DATE` | DATETIME |  | This column stores the date when the requisition was printed using the Specimens section and its copies. |
| 15 | `SENT_TIME` | DATETIME (Local) |  | This column stores the time when the requisition was printed using the Specimens section and its copies. |
| 16 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 17 | `PAT_CSN` | NUMERIC | FK→ | This column stores the patient's contact serial number. |
| 18 | `DELETE_REASON_C_NAME` | VARCHAR | org | This column will hold the reason for deleting the specimen record. |
| 19 | `RECORD_CREATION_DT` | DATETIME |  | Stores the date the record was created. |
| 20 | `INSTANT_OF_UPD_TM` | DATETIME (Local) |  | Stores the instant the record was last locked/unlocked. |
| 21 | `FROZEN_YN` | VARCHAR |  | Indicates if the specimen is frozen. |
| 22 | `SPEC_LABEL_PRT_DTTM` | DATETIME (Local) |  | The most recent instant that a label was printed for the specimen. It is updated every time a label is printed for the specimen. |
| 23 | `EPISODE_ID` | NUMERIC | FK→ | Stores Diagnose Behandel Combinatie (DBC) Episode linked to a specimen in DBC enabled environments. |
| 24 | `MARKED_AS_SENT_DTTM` | DATETIME (Local) |  | This is the instant that the specimen is marked as sent to Lab. |
| 25 | `IN_FIXATIVE_DTTM` | DATETIME (UTC) |  | Enter time when specimen was fixed in fixative (example:formalin). This is applicable only if specimen is indicated as fixed in fixative or fixed in formalin. |
| 26 | `LOG_ID` | VARCHAR | shared | This item stores the surgical log where this specimen is collected and documented. |
| 27 | `AUTHRZING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 28 | `CLINICAL_IMPRESSION` | VARCHAR |  | Free text clinical impressions for the specimen. |
| 29 | `LATERALITY_C_NAME` | VARCHAR | org | The category ID for the laterality of the specimen. |
| 30 | `SPECIMEN_WEIGHT` | NUMERIC |  | This column stores the specimen weight. |
| 31 | `SPECIMEN_UNIT_C_NAME` | VARCHAR | org | This item is used to indicate the unit corresponding to the specimen weight documented. |
| 32 | `OTHER_REC_CREATE_WF_C_NAME` | VARCHAR |  | Store workflows other than specimen navigator which created this record |
| 33 | `SPECIMEN_SIZE` | NUMERIC |  | This item is used to document the size of the specimen collected. |
| 34 | `SPECIMEN_SIZE_UNIT_C_NAME` | VARCHAR | org | This item is used to indicate the unit corresponding to the specimen size documented. |
| 35 | `SOURCE_MODIFIER_C_NAME` | VARCHAR | org | This item documents an additional modifier to the specimen's source. |
| 36 | `CALCIFICATION_SPREADING` | INTEGER |  | This column stores the spread of calcification in mm. |
| 37 | `NUMBER_OF_TUMORS` | INTEGER |  | This column stores the number of tumors. |
| 38 | `TUMOR_1_DISTANCE_FROM_PAP` | INTEGER |  | This column stores the distance of tumor 1 from the papilla in mm. |
| 39 | `TUMOR_1_SIZE` | INTEGER |  | This column stores the size of tumor 1 in mm. |
| 40 | `TUMOR_2_DISTANCE_FROM_PAP` | INTEGER |  | This column stores the distance of tumor 2 from the papilla in mm. |
| 41 | `TUMOR_2_SIZE` | INTEGER |  | This column stores the size of tumor 2 in mm. |
| 42 | `TUMOR_3_DISTANCE_FROM_PAP` | INTEGER |  | This column stores the distance of tumor 3 from the papilla in mm. |
| 43 | `TUMOR_3_SIZE` | INTEGER |  | This column stores the size of tumor 3 in mm. |
| 44 | `TUMOR_4_DISTANCE_FROM_PAP` | INTEGER |  | This column stores the distance of tumor 4 from the papilla in mm. |
| 45 | `TUMOR_4_SIZE` | INTEGER |  | This column stores the size of tumor 4 in mm. |
| 46 | `TUMOR_5_DISTANCE_FROM_PAP` | INTEGER |  | This column stores the distance of tumor 5 from the papilla in mm. |
| 47 | `TUMOR_5_SIZE` | INTEGER |  | This column stores the size of tumor 5 in mm. |
| 48 | `SPECIMEN_VOLUME` | NUMERIC |  | This column stores specimen volume. |
| 49 | `SPECIFY_MATERIAL_FT` | VARCHAR |  | This column stores the material that was removed. |
| 50 | `ENDOSCOPIC_FINDINGS_FT` | VARCHAR |  | This column stores the endoscopic findings of a specimen. |
| 51 | `DISTANCE_TO_BORDER` | INTEGER |  | This column stores the distance to the border, in mm. |
| 52 | `MEDICAL_TREATMENT_FT` | VARCHAR |  | This column stores the medical treatment needed if necessary. |
| 53 | `SIZE_OF_TUM_ULTRASOUND` | INTEGER |  | The size of the tumor in mm, discovered via ultrasound. |
| 54 | `SIZE_OF_TUMOR_MAMMOGRAPHY` | INTEGER |  | The size of the tumor in mm, discovered via mammography. |
| 55 | `SPECIMEN_READING` | NUMERIC |  | This item stores the radiologic reading for a specimen. |
| 56 | `PRIORITY_DUE_UTC_DTTM` | DATETIME (UTC) |  | Stores the due date and time for a specimen priority. |
| 57 | `TOTAL_NUMBER_OF_CORES` | INTEGER |  | For needle biopsy procedures, stores the total number of cores taken. |
| 58 | `NUM_OF_CORES_W_CALCIFICATION` | INTEGER |  | For needle biopsy procedures, stores the number of cores taken with calcification. |
| 59 | `PROTOCOL_ID_STRING` | VARCHAR |  | Stores a free text ID for research protocols. |
| 60 | `ID_PREFIX` | VARCHAR |  | Short name of the group that the specimen falls under (e.g. clinical, pathology, etc.). |
| 61 | `USER_MOD_SPEC_ID_YN` | VARCHAR |  | Flag that stores whether or not a user manually modified the specimen ID. |
| 62 | `SPECIMEN_ORIENTATION_FREE_TEXT` | VARCHAR |  | Stores the orientation of the specimen. |
| 63 | `SPECIMEN_TISSUE_EXCISION_DTTM` | DATETIME (UTC) |  | Stores when a specimen was excised. |
| 64 | `SPECIMEN_NUMBER_OF_CONTAINERS` | INTEGER |  | Stores the number of containers used for storing the specimen. |
| 65 | `NEEDLE_GAUGE` | INTEGER |  | Stores the gauge of the needle used when retrieving a specimen. |
| 66 | `NUMBER_OF_PASSES` | INTEGER |  | Stores the number of passes performed when retrieving a specimen. |
| 67 | `NUMBER_OF_SLIDES` | INTEGER |  | Stores the number of slides used when collecting a specimen. |
| 68 | `REASON_FOR_VISIT` | VARCHAR |  | Stores the reason for the patient visit as documented on a surgical specimen. This documentation is for reference only and does not update any diagnosis or problem list documentation. |
| 69 | `DISTANCE_FROM_NIPPLE` | INTEGER |  | Stores the distance from the nipple to the specimen collection site. |
| 70 | `MAN_REL_TO_MYCHRT_YN` | VARCHAR |  | This item indicates whether the order result of the specimen should be manually released to MyChart. |
| 71 | `MATERIAL_SUPPLEMENTARY_DESC` | VARCHAR |  | The supplementary description of the material. |
| 72 | `PLACENTA_WEIGHT` | NUMERIC |  | The weight of the placenta. |
| 73 | `MEMBRANE_CONDITION` | VARCHAR |  | The condition of the membrane. |
| 74 | `MARKING_OF_UMBILICAL_CORD` | VARCHAR |  | The marking of the umbilical cord. |
| 75 | `GESTATIONAL_AGE_IN_WEEKS` | INTEGER |  | The gestational age in weeks. |
| 76 | `EXTERNAL_SPECIMEN_IDENT` | VARCHAR |  | The external identifier for this specimen collection record. |
| 77 | `SUGGESTED_SPECIMEN_SOURCE_C_NAME` | VARCHAR |  | If the specimen was generated from a suggestion, the source that was suggested. |
| 78 | `SUGGESTED_SPECIMEN_TYPE_C_NAME` | VARCHAR |  | If the specimen was generated from a suggestion, the type that was suggested. |
| 79 | `SPECIMEN_TRANSPORT_UTC_DTTM` | DATETIME (UTC) |  | This column stores the moment a specimen was picked up for transport as a date/time instant. |
| 80 | `COLD_ISCHEMIA_DURATION` | INTEGER |  | This column stores the time between specimen collection and fixation. |
| 81 | `ASSOCIATED_PROC_ORDER_ID` | NUMERIC |  | The ID of the order for the procedure that the specimen is associated with. This is expected to generally be the procedure during which the specimen was collected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

