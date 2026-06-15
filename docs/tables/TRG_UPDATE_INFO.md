# TRG_UPDATE_INFO

> Table for overtime single items.

**Primary key:** `REGIMEN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 39  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique identifier for the patient order group record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DT` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `CONTACT_NUM` | VARCHAR |  | The number of the contact |
| 6 | `LINKED_ORDER_TYPE_C_NAME` | VARCHAR |  | Stores the link type for the patient order group's (TLG) source order group (OSQ) that represents a linked group. |
| 7 | `INST_OF_ENTRY_DTTM` | DATETIME (Local) |  | Instant at which the contact was created. |
| 8 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 9 | `PROD_ACQ_TARGET_CELL_DOSE` | NUMERIC |  | Stores the target product acquisition cell dose. |
| 10 | `PROD_ACQ_MIN_CELL_DOSE` | NUMERIC |  | Stores the minimum product acquisition cell dose. |
| 11 | `PROD_ACQ_CELL_DOSE_UNITS_C_NAME` | VARCHAR | org | Stores the units of the target and minimum cell doses for the product acquisition. |
| 12 | `PROD_ACQ_CELL_SOURCE_C_NAME` | VARCHAR | org | The source of the cells of the product acquisition. |
| 13 | `COND_PALIFERMIN_YN` | VARCHAR |  | Whether or not Palifermin is planned. |
| 14 | `COND_PLANNED_TOTAL_DOSE` | NUMERIC |  | The Planned Total Dose (cGy) for the conditioning regimen. |
| 15 | `COND_SETTING_C_NAME` | VARCHAR | org | The setting of the conditioning regimen. |
| 16 | `COND_INTENT_C_NAME` | VARCHAR | org | The intent of the conditioning regimen. |
| 17 | `COND_RAD_FRACT_YN` | VARCHAR |  | Whether or not Radiation Fractionate is planned. |
| 18 | `GVHD_OTHER_DRUG` | VARCHAR |  | The free-text description for the other GVHD drug. |
| 19 | `COND_OTH_DRUG` | VARCHAR |  | The free-text description for the other conditioning drug. |
| 20 | `PROD_ACQ_OTH_PROC_METHOD` | VARCHAR |  | The free-text description for the other product process method. |
| 21 | `INSTANT_OF_EDIT_DTTM` | DATETIME (Local) |  | The instant data was edited. |
| 22 | `PROD_ACQ_CELL_SOURCE_OTHER` | VARCHAR |  | Free text cell source. Used when Cell Source (TRG 33104) is 999-Other Cells. |
| 23 | `IEC_CELL_MANUFACTURING_SITE_C_NAME` | VARCHAR | org | The IEC cell manufacturing site. |
| 24 | `IEC_OTHER_CELL_MFG_SITE` | VARCHAR |  | The other cell manufacturing site. |
| 25 | `IEC_BIOTECH_COMPANY_C_NAME` | VARCHAR | org | The biotech company manufacturing the IEC product. |
| 26 | `IEC_OTHER_BIOTECH_COMPANY` | VARCHAR |  | The other biotech company manufacturing the IEC product. |
| 27 | `IEC_CELL_COLLECTION_DATE` | DATETIME |  | The date on which the cells will be collected from the patient. |
| 28 | `IEC_CELL_SHIP_DATE` | DATETIME |  | The date on which the collected cells will be shipped to the cell manufacturing company or lab. |
| 29 | `IEC_PRODUCT_RETURN_DATE` | DATETIME |  | The date on which the manufactured cell therapy product is expected to be returned from the manufacturing company or lab. |
| 30 | `IEC_PROD_OUT_OF_SPEC_YN` | VARCHAR |  | Indicates whether the manufactured cell therapy product is out of specification. |
| 31 | `IEC_OTHER_BRIDGING_THERAPY` | VARCHAR |  | The other IEC bridging therapy. |
| 32 | `IEC_BRIDGE_THERAPY_START_DATE` | DATETIME |  | The planned start date of the IEC bridging therapy. |
| 33 | `IEC_BRIDGE_THERAPY_END_DATE` | DATETIME |  | The planned end date of the IEC bridging therapy. |
| 34 | `IEC_OTHER_TOXICITY_TREATMENTS` | VARCHAR |  | The other planned toxicity treatments after IEC infusion. |
| 35 | `IEC_OTHER_EFFICACY_TREATMENTS` | VARCHAR |  | The other planned efficacy treatments after IEC infusion. |
| 36 | `CELL_TYPE_OTHER` | VARCHAR |  | The planned other cell type to be collected for the immune effector cell therapy (IEC) infusion. |
| 37 | `IEC_NO_BRIDGING_YN` | VARCHAR |  | Indicates the affirmation that no bridging therapy is planned. |
| 38 | `CND_OTHR_RAD` | VARCHAR |  | The free-text description for the other radiation field. |
| 39 | `CND_OTHR_RAD_BOOST` | VARCHAR |  | The free-text description for the other radiation boost field. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

