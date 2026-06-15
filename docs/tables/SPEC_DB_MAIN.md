# SPEC_DB_MAIN

> The SPEC_DB_MAIN table contains basic information about your specimen records. These include clinical pathology, anatomic pathology, and quality control specimens. One row in this table represents one specimen.

**Primary key:** `SPECIMEN_ID`  
**Columns:** 62  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique ID of the specimen record |
| 2 | `SPEC_NUMBER_LN1` | VARCHAR |  | The main external identifier of the specimen |
| 3 | `SPEC_DTM_COLLECTED` | DATETIME (Local) |  | The date and time when the specimen was collected. |
| 4 | `SPEC_DTM_RECEIVED` | DATETIME (Local) |  | The date and time when the specimen was received. |
| 5 | `SPEC_CONTAINER_ID` | VARCHAR |  | The unique identifier of the container associated with this specimen |
| 6 | `SPEC_CONTAINER_ID_CONTAINER_TYPE_NAME` | VARCHAR |  | The name of the container type record. |
| 7 | `SPEC_SOURCE_C_NAME` | VARCHAR | org | The specimen source category for the specimen. |
| 8 | `SPEC_EPT_PAT_ID` | VARCHAR | FK→ | The unique identifier of the patient whom this specimen belongs to. |
| 9 | `SPEC_SUB_SPEC_NO` | VARCHAR |  | The submitter's specimen number. |
| 10 | `SPEC_DRAW_TYPE_C_NAME` | VARCHAR | org | The draw type category number for the specimen |
| 11 | `SPEC_REQ_GRP_ID` | NUMERIC |  | The unique ID of the requisition grouper associated with this specimen if this is a non-EPT patient |
| 12 | `REQ_SMT_ID` | NUMERIC |  | The unique identifier of the submitter that collected this specimen. This is only populated for reference lab specimens. |
| 13 | `REQ_SMT_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 14 | `REQ_ID` | NUMERIC |  | The unique identifier of the requisition this specimen is attached to. This is only populated for reference lab specimens. |
| 15 | `ACUTE_CONVAL_C_NAME` | VARCHAR |  | The acute/convalescent category number for the specimen record. |
| 16 | `CASE_ID` | NUMERIC | shared | The unique identifier of the case this specimen is attached to. This is only populated for anatomic pathology specimens. |
| 17 | `RECV_QUEUE_COMM_ID` | VARCHAR |  | The unique ID of the internal receiving comment that is associated with this specimen. |
| 18 | `SPEC_COLL_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the specimen was collected in the UTC time zone. |
| 19 | `SPEC_RCVD_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the specimen was received in the UTC time zone. |
| 20 | `SPEC_FROZEN_YN` | VARCHAR |  | Indicates whether this specimen is a frozen specimen. |
| 21 | `SPECIMEN_COL_ID` | NUMERIC |  | The unique identifier of the specimen collection record which is associated with this specimen. |
| 22 | `AP_RECEIVE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the anatomic pathology specimen was received in the UTC time zone. This is only populated for anatomic pathology specimens. |
| 23 | `DRAW_SESS_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the draw session this specimen belongs to was started. It is stored in the UTC time zone. |
| 24 | `SPECIMEN_TYPE_C_NAME` | VARCHAR | org | The specimen type category ID for the specimen. This is calculated from the specimen type for the first order on the specimen that has a specimen type set and has not been redrawn or removed. If all orders on the specimen have been redrawn or removed, it is calculated from the specimen type for the first removed order that has a specimen type set. |
| 25 | `SPEC_FROM_DSL_YN` | VARCHAR |  | Stores whether a specimen was created from the Specimen Linking activity. The default value is No. |
| 26 | `ONSET_DATE` | DATETIME |  | The onset date that symptoms began for the associated specimen. This is a legacy item and this data is no longer populated in Chronicles. |
| 27 | `BIOHAZARD_C_NAME` | VARCHAR |  | The biohazard category ID for the specimen. This is legacy data that is no longer populated. |
| 28 | `DRAW_CHGS_TRGRD_YN` | VARCHAR |  | Indicates whether draw charges have been triggered for the specimen. 'Y' indicates that a draw charge has been triggered. 'N' or NULL indicate that a draw charge has not been triggered. |
| 29 | `SPEC_SOURCE` | VARCHAR |  | The specimen source for the specimen. This is legacy data that is no longer populated. |
| 30 | `SPEC_ORIGIN_C_NAME` | VARCHAR |  | The special specimen origin category ID for the specimen. |
| 31 | `IMPORT_RUN_BATCH_NUMBER_ID` | VARCHAR |  | The batch ID associated to an imported specimen |
| 32 | `CREATION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 33 | `COLL_PPID_OVRIDE_YN` | VARCHAR |  | Indicates whether PPID was overridden during collection for this specimen. |
| 34 | `COLL_PSID_OVRIDE_YN` | VARCHAR |  | Indicates whether PSID was overridden during collection for this specimen. |
| 35 | `REQ_OR_GEN_SUBMITTER_ID` | NUMERIC |  | The unique identifier of the submitter of the requisition that this specimen is attached to. This is only populated for reference lab specimens. This will include a generic submitter that is placed on orders that were placed at your organization and collected at an EpicCare Link site. |
| 36 | `REQ_OR_GEN_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 37 | `COLL_PRTR_OVRIDE_YN` | VARCHAR |  | Indicates whether a required printer scan was overridden. 'Y' indicates that a printer scan was overridden during the collection process. 'N' or NULL indicates that the printer scan was completed or not required. |
| 38 | `COLL_PPID_REQ_YN` | VARCHAR |  | Indicates if positive patient identification (PPID) was required during the collection process (printing labels or collection documentation). Workflows that never require PPID (for example, Requisition Entry) will not populate this item. |
| 39 | `COLL_PSID_REQ_YN` | VARCHAR |  | Indicates if positive specimen identification (PSID) was required during collection documentation. Workflows that never require PSID (for example, Requisition Entry) will not populate this item. |
| 40 | `SPECIAL_ABO_PHENOTYPE_C_NAME` | VARCHAR |  | The nonstandard ABO category ID for the blood product specimen. |
| 41 | `INTENDED_USE_ATTRIBUTE_C_NAME` | VARCHAR |  | The indended use category ID for the blood product specimen. |
| 42 | `BLOOD_GROUP_SPEC_MSG_C_NAME` | VARCHAR |  | The blood groups special message category ID for the blood product specimen. |
| 43 | `COLLECTION_TYPE_CODE_C_NAME` | VARCHAR |  | The collection type category ID for the donor product specimen. |
| 44 | `PRODUCT_COLLECTION_DATE` | DATETIME |  | The date at which this blood product specimen was collected. This column is populated only for certain blood product types, according to the ISBT-128 specification. |
| 45 | `PRODUCT_COLLECTION_UTC_DTTM` | DATETIME (UTC) |  | The date and time at which this blood product specimen was collected. This column is populated only for certain blood product types, according to the ISBT-128 specification. |
| 46 | `SPECIAL_TESTING_CODE_C_NAME` | VARCHAR |  | The special testing "N-Code" category ID for the blood product specimen. |
| 47 | `RBC_ANTIGEN_BARCODE` | VARCHAR |  | Stores a barcoded string containing antigen test info for RBC blood product specimens, according to the ISBT-128 specification. |
| 48 | `PLATELET_ANTIGEN_BARCODE` | VARCHAR |  | Stores a barcoded string with information about platelet HLA and HPA testing for a blood product specimen, according to the ISBT-128 specification. |
| 49 | `COLL_TIMER_EXPIRATIONS` | INTEGER |  | Indicates how many times a scan workflow timer expired after accessioning for this specimen. |
| 50 | `PROD_DESC_CODE_ID` | NUMERIC |  | The unique ID of the product description code corresonding to this donor product specimen, according to the ISBT-128 specification. |
| 51 | `PROD_DESC_CODE_ID_PROD_DESC_CODE_NAME` | VARCHAR |  | Name of the product description code. |
| 52 | `EXPIRATION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time at which this specimen expires. |
| 53 | `FACILITY_IDENTIFIER_RECORD_ID` | NUMERIC |  | Unique ID of the submitter corresponding to the donor facility that prepared this product specimen. |
| 54 | `FACILITY_IDENTIFIER_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 55 | `DESC_CODE_CSN_ID` | NUMERIC |  | Stores the CSN of the product description code for this row. |
| 56 | `ABO_PHENOTYPE_C_NAME` | VARCHAR |  | Stores the ABO blood group type for a blood product specimen, as encoded by a Blood Groups barcode (I OVS 76010). |
| 57 | `RHD_LAB_ANTIGEN_RESULT_C_NAME` | VARCHAR |  | Stores the RhD type for a blood product specimen, as encoded by a Blood Groups barcode (I OVS 76010). |
| 58 | `PRODUCT_STATUS_C_NAME` | VARCHAR |  | Contains the status of a product specimen |
| 59 | `SPEC_CUMULATIVE_VOLUME` | INTEGER |  | The cumulative volume of all containers on the specimen, in milliliters |
| 60 | `DEST_EPT_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record this product is destined to be administered to, regardless of whether or not the administration has happened yet |
| 61 | `DEST_REQ_GROUPER_ID` | NUMERIC |  | The unique ID of the grouper this product is destined to be administered to, regardless of whether or not the administration has happened yet |
| 62 | `SPECIAL_RHD_PHENOTYPE_C_NAME` | VARCHAR |  | Stores nonstandard RhD information for a blood product specimen, as encoded by the Blood Groups barcode (I OVS 76010). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DEST_EPT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `SPEC_EPT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

