# OR_IMP_3

> The OR_IMP_3 table contains implant information.

**Overflow of:** [OR_IMP](OR_IMP.md)  
**Primary key:** `IMPLANT_ID`  
**Columns:** 32  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `EXTRACARD_VLT` | NUMERIC |  | This item stores the voltage measured for the extracardiac stimulation |
| 3 | `EXTRACARD_PULSE` | NUMERIC |  | This item stores pulse width for the extracardiac stimulation |
| 4 | `PREVIOUS_OPERATION_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `SUPPORT_NET_YN` | VARCHAR |  | Indicates whether a support net was used for this implant. Y indicates that a support net was used. An N or null value indicates a support net was not used. |
| 6 | `SCREW_COUNT` | INTEGER |  | The count of screws used by this implant. |
| 7 | `SCREW_HOLE_C_NAME` | VARCHAR | org | The screw hole category ID for the implant. |
| 8 | `CORE_PLUG_YN` | VARCHAR |  | Indicates whether a core plug was used for this implant. Y indicates a core plug was used. An N or a null value indicates a core plug was not used. |
| 9 | `EAN_NUMBER` | VARCHAR |  | Stores the European Article Number (EAN) for an implant. |
| 10 | `IMPLANT_SOURCE_C_NAME` | VARCHAR | org | This item stores the source of the implant for the patient. |
| 11 | `PACEMAKER_AFFECT` | VARCHAR |  | This free text item will allow the provider to document what will happen to the mode and rate when a magnet is placed. |
| 12 | `AICD_MAGNET_AFFECT` | VARCHAR |  | This item is used to document what will happen when a magnet is placed properly. |
| 13 | `SEC_COUNTRY_IDENTIFIER` | VARCHAR |  | The country identifier present in the Donation Identification Sequence of the Single European Code (SEC) for an implant. |
| 14 | `SEC_TISSUE_ESTABLISHMENT_CODE` | VARCHAR |  | The tissue establishment code present in the Donation Identification Sequence of the Single European Code (SEC) for an implant. |
| 15 | `SEC_UNIQUE_DONATION_NUMBER` | VARCHAR |  | The unique donation number present in the Donation Identification Sequence of the Single European Code (SEC) for an implant. |
| 16 | `SEC_CODING_SYSTEM_IDENTIFIER_C_NAME` | VARCHAR | org | The coding system identifier present in the Production Identification Sequence of the Single European Code (SEC) for an implant. |
| 17 | `SEC_PRODUCT_CODE` | VARCHAR |  | The product code present in the Production Identification Sequence of the Single European Code (SEC) for an implant. |
| 18 | `SEC_SPLIT_NUMBER` | VARCHAR |  | The split number present in the Production Identification Sequence of the Single European Code (SEC) for an implant. |
| 19 | `FLOW_RATE` | NUMERIC |  | Stores implant flow rate setting. |
| 20 | `PRESSURE` | NUMERIC |  | Stores implant pressure setting. |
| 21 | `NUMBER_ACCESSORIES_USED` | INTEGER |  | This item stores the number of accessories used. |
| 22 | `IMPLANT_LENGTH` | NUMERIC |  | This column stores the length of the implant. |
| 23 | `TISS_IMPL_UTC_DTTM` | DATETIME (UTC) |  | Instant that the tissue was implanted into the patient. Intended to be used with a third-party tissue tracking system. |
| 24 | `IMPLANT_BRAND_C_NAME` | VARCHAR | org | The brand of the implantable device. |
| 25 | `CALIBRATION_DATE` | DATETIME |  | Date the implant or seed was calibrated or made radioactive. |
| 26 | `RADIOACTIVE_ACTIVITY` | NUMERIC |  | The measured amount of radioactivity in the implant. |
| 27 | `NHR_LEAD_TYPE_C_NAME` | VARCHAR |  | The type of lead, how this lead is used. Source: NHR |
| 28 | `EXPLANT_REPL_STATUS_C_NAME` | VARCHAR | org | The explant replacement status. |
| 29 | `EXPLANT_REPL_IMPLANT_ID` | VARCHAR |  | The explant replacement ID. |
| 30 | `IMPLANT_WIDTH` | NUMERIC |  | This column stores the width of the implant. |
| 31 | `WOUND_LENGTH` | NUMERIC |  | This column stores the length of the wound. |
| 32 | `WOUND_WIDTH` | NUMERIC |  | This column stores the width of the wound. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

