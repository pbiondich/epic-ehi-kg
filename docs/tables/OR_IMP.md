# OR_IMP

> The OR_IMP table contains implant information.

**Overflow family:** [OR_IMP_2](OR_IMP_2.md), [OR_IMP_3](OR_IMP_3.md)  
**Primary key:** `IMPLANT_ID`  
**Columns:** 57  
**Org-specific columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique ID of the implant record. |
| 2 | `IMPLANT_NAME` | VARCHAR |  | The name of the implant record. |
| 3 | `IMPLANT_TYPE_C_NAME` | VARCHAR | org | The implant type category number for the implant record. |
| 4 | `MANUFACTURER_C_NAME` | VARCHAR | org | The manufacturer category number for the implant record. |
| 5 | `STATUS_C_NAME` | VARCHAR | org | The implant status category number for the implant record. |
| 6 | `SMDA_YN` | VARCHAR |  | Indicates whether the implant conforms to the Safe Medical Device Act (SMDA). Y indicates that the implant conforms to the SMDA. A null indicates that no value is documented. N indicates that the implant does not conform to the SMDA. |
| 7 | `ACTIVE_YN` | VARCHAR |  | Indicates whether the implant record is active. Y indicates that the implant is active. A null indicates that no value is documented. N indicates that the implant is not active. |
| 8 | `MODEL_NUMBER` | VARCHAR |  | The model number of the implant. |
| 9 | `SERIAL_NUMBER` | VARCHAR |  | The serial number of the implant. |
| 10 | `LOT_NUMBER` | VARCHAR |  | The lot number of the implant. |
| 11 | `EXPIRATION_DATE` | DATETIME |  | The expiration date of the implant. |
| 12 | `RECEIVED_DATE` | DATETIME |  | The date the implant was received. |
| 13 | `RECPT_NOTIFY_DATE` | DATETIME |  | The date the manufacturer was notified of implant receipt. |
| 14 | `RECALLED_DATE` | DATETIME |  | The date the implant was recalled. |
| 15 | `RECALLED_NOT_DATE` | DATETIME |  | The date the manufacturer was notified of implant recall. |
| 16 | `PAT_EXPIRY_DATE` | DATETIME |  | The date the patient with the implant expired. |
| 17 | `PAT_EXP_NOTIF_DATE` | DATETIME |  | The date the manufacturer was notified of the patient's expiration. |
| 18 | `INVENTORY_ITEM_ID` | VARCHAR |  | The unique ID of the supply linked to the implant record. |
| 19 | `INVENTORY_ITEM_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 20 | `PACEMAKER_RATE` | NUMERIC |  | The pacemaker rate of the implant. |
| 21 | `IMPLANT_AREA_C_NAME` | VARCHAR | org | The implant area category number for the implant record. |
| 22 | `PASS_THROUGH_CODE` | VARCHAR |  | The pass through code used for billing. |
| 23 | `CHARGE_CODE_EAP_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 24 | `IMPLANT_SIZE` | VARCHAR |  | The size of the implant. |
| 25 | `TISSUE_TYPE_C_NAME` | VARCHAR | org | The tissue type category number for the implant record. |
| 26 | `PREP_START_DTTM` | DATETIME (Attached) |  | The date and time when the tissue preparation was started. |
| 27 | `IMPLANT_TEMP` | NUMERIC |  | Temperature at implantation of tissue, in degrees Fahrenheit. |
| 28 | `INFECTED_DATE` | DATETIME |  | The date the tissue was infected. |
| 29 | `SURG_NOTIFIED_DATE` | DATETIME |  | The date the surgeon was notified about the infection. |
| 30 | `TISSUE_YN` | VARCHAR |  | Indicates whether this is a tissue implant. Y indicates that this is a tissue implant. A null indicates that no value is documented. N indicates that this is not a tissue implant. |
| 31 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this implant. This column is frequently used to link to the PATIENT table. |
| 32 | `IMPLANT_LAT_C_NAME` | VARCHAR | org | The laterality category number for the implant record. |
| 33 | `PACE_INITIAL_YN` | VARCHAR |  | Indicates whether this pacemaker is the initial device implanted in a patient. Y indicates that this is the initial device. A null indicates that no value is documented. N indicates that this is not the initial device. |
| 34 | `PACE_POCKET_LOC_C_NAME` | VARCHAR | org | The category number for the pocket location in which this pacemaker is implanted. |
| 35 | `TEMP_PACE_YN` | VARCHAR |  | Indicates whether this is a temporary pacemaker. Y indicates that this is a temporary pacemaker. A null indicates that no value is documented. N indicates that this is not a temporary pacemaker. |
| 36 | `PACE_PREVENTION_C_NAME` | VARCHAR | org | The prevention type category number for the implant record. Only stores the prevention type if the implant type is pacemaker. |
| 37 | `TEMP_PACE_CHAMBER_C_NAME` | VARCHAR | org | The temporary pacemaker chamber category number for the implant record. |
| 38 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category number for the implant record. |
| 39 | `MANUF_NUM` | VARCHAR |  | The manufacturer number of the supply linked to the implant record. |
| 40 | `SUP_CAT_NUM` | VARCHAR |  | The supplier catalog number of the supply linked to the implant record. |
| 41 | `PREP_INSTR_SOURCE_C_NAME` | VARCHAR | org | The "source of tissue preparation instructions" category number for the tissue implant. |
| 42 | `STATIC_UDI` | VARCHAR |  | The static piece of the unique device identifier, obtained from the implant barcode. This is the Global Trade Item Number (GTIN) for General Specifications (GS1) barcodes and the combination of the labeler identification code and the catalog number for Health Industry Bar Code (HIBC) barcodes. |
| 43 | `STATIC_UDI_TYPE_C_NAME` | VARCHAR |  | The type of the static unique device identifier, based on the format of the barcode it was obtained from. |
| 44 | `TISSUE_AUTOLOGOU_YN` | VARCHAR |  | Stores whether a tissue implant was taken from the patient. |
| 45 | `EXPLANT_DISPOSITN_C_NAME` | VARCHAR | org | This item stores the where the implant was sent after being explanted. |
| 46 | `SKIN_SUB_USAGE_C_NAME` | VARCHAR | org | Document how the skin substitute was used. |
| 47 | `SKIN_SUB_AREA_USED` | NUMERIC |  | Document the area of the skin substitute used. |
| 48 | `SKIN_SUB_AREA_WASTE` | NUMERIC |  | Document the area of the skin substitute wasted. |
| 49 | `TISSUE_INSPC_RSLT_C_NAME` | VARCHAR | org | Document result of inspecting the tissue |
| 50 | `RADIOACTIVE_C_NAME` | VARCHAR | org | This field will be used by the nurse to document when an implant is radioactive. |
| 51 | `REPLACE_EXISTING_C_NAME` | VARCHAR |  | This column displays whether the given implant is replacing an existing implant. |
| 52 | `TISSUE_EXPANDER_VOLUME` | NUMERIC |  | The volume (mL) the tissue expander was inflated. |
| 53 | `REMOVE_BY_DATE` | DATETIME |  | Date implant needs to be removed from patient. |
| 54 | `IMPLANT_VOLUME` | NUMERIC |  | This documents the volume of the implant. |
| 55 | `IMP_VOLUME_UNIT_C_NAME` | VARCHAR | org | Choose which unit to use for volume measurements. |
| 56 | `SUPPLY_TYPE_C_NAME` | VARCHAR | org | This is the type of inventory item for the implant. This is used for one-time implants, which do not have an inventory item, to determine what markup table to use for charging. |
| 57 | `EXPLANT_WARRANTY_COMPLETION_DT` | DATETIME |  | This item stores the explant warranty completion date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

