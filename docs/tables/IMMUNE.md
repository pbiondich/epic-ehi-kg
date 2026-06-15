# IMMUNE

> The IMMUNE table contains data for immunizations ordered through clinical system. May also contain information on immunizations as reported by patient, but not ordered/administered via clinical system; Fields in this table are noadd- single items in database. If an immunization record is edited/changed, that record will be re-extracted and reflect the updated values.

**Primary key:** `IMMUNE_ID`  
**Columns:** 50  
**Org-specific columns:** 9  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMMUNE_ID` | NUMERIC | PK | The unique ID of the immunization record in your system production system. |
| 2 | `IMMUNZATN_ID` | NUMERIC | FK→ | The ID of the immunization record that corresponds to the type of immunization given to this patient. |
| 3 | `IMMUNZATN_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 4 | `IMMUNE_DATE` | DATETIME |  | The date the immunization was administered in calendar format. |
| 5 | `DOSE` | VARCHAR |  | The immunization dosage. |
| 6 | `ROUTE_C_NAME` | VARCHAR | org | The category value associated with the route of the immunization, such as oral, intramuscular, or intradermal. |
| 7 | `SITE_C_NAME` | VARCHAR | org | The category value associated with the location of the injection, if appropriate. For example, left gluteus or right deltoid. |
| 8 | `MFG_C_NAME` | VARCHAR | org | The category value associated with the manufacturer of this vaccine. |
| 9 | `LOT` | VARCHAR |  | The lot number of the vaccine. |
| 10 | `EXP_DATE` | DATETIME |  | The date the immunization is next due, if in a series. This is manually established by the user, and not automatically calculated like an HM or advisory. |
| 11 | `GIVEN_BY_USER_ID` | VARCHAR |  | The unique ID of the system user who administered the immunization. This ID may be encrypted. |
| 12 | `GIVEN_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the system user who ordered the immunization. This ID may be encrypted. NOTE: If an immunization record is edited/updated, this will show the most recent change user ID. |
| 14 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `ENTRY_DATE` | DATETIME |  | The date the immunization was recorded in the patient’s chart in calendar format. NOTE: If an immunization record is edited/updated, this will show the most recent change date. |
| 16 | `EXPIRATION_DATE` | DATETIME |  | Date upon which this immunization expires |
| 17 | `EXTERNAL_ADMIN_C_NAME` | VARCHAR | org | Category value indicating the source of verification of external administration of immunization, e.g. patient reported, WIR reported, etc. |
| 18 | `VIS_DATE_TEXT` | VARCHAR |  | The date on the vaccine information statement. Note that this is a free text field in the application, so data will not be in standard datetime format. |
| 19 | `DEFER_REASON_C_NAME` | VARCHAR | org | Category value indicating the reason for deferring the immunization, e.g. patient refused, contraindication, etc. |
| 20 | `MED_ADMIN_COMMENT` | VARCHAR |  | Free text comment regarding the administration of this immunization |
| 21 | `PHYSICAL_SITE` | VARCHAR |  | Item that stores the physical location where the immunization was administered like some specific hospital |
| 22 | `IMM_PRODUCT` | VARCHAR |  | Item which stores the product of the immunization. Products are usually related to the lot number. |
| 23 | `IMMUNIZATION_TIME` | DATETIME (Local) |  | Column that stores the time when a given immunization was administered. |
| 24 | `NDC_NUM_ID` | VARCHAR |  | Store the NDC number ID associated with the administration |
| 25 | `NDC_NUM_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 26 | `DOCUMENT_DCS_ID` | VARCHAR |  | Document ID for the immunization. This is the information stored when the e-sign information is selected. |
| 27 | `ORDER_ID` | NUMERIC | shared | Order ID for immunization ordered. |
| 28 | `IMM_ANSWER_ID` | VARCHAR |  | Stores answers for immunization questions. |
| 29 | `IMMNZTN_STATUS_C_NAME` | VARCHAR |  | The category value associated with "Given" if the immunization has been administered, "Deleted" if the immunization has been deleted from the administration history, "Incomplete" if the item has been ordered but not administered and a status of "Deferred" if the immunization has been deferred. |
| 30 | `IMM_MAR_ADMIN_LINE` | INTEGER |  | The line number in the linked order record's immunization link item (I ORD 11270) which references this immunization record ID. |
| 31 | `IMM_CHARGE_REC_ID` | VARCHAR |  | This column contains the UCL (Universal Charge Line) record ID for the immunization charge. |
| 32 | `IMM_CSN` | NUMERIC |  | This column contains the CSN (contact serial number) for the immunization. |
| 33 | `EXTERNAL_ID` | VARCHAR |  | This column contains the immunization's external ID, which is populated by the interface. The external ID is the external system's identifier for the immunization. |
| 34 | `EXTERNAL_SYSTEM` | VARCHAR |  | This column contains the name or ID of the third party system that the immunization data came from. This item is only populated by custom import specifications. |
| 35 | `INSTANT_OF_ENT_DTTM` | DATETIME (Local) |  | This column contains the last instant of update of the immunization problem list (LPL) record. |
| 36 | `IMM_HISTORIC_ADM_YN` | VARCHAR |  | Indicates whether the immunization administration is a historical administration. |
| 37 | `IMMNZTN_DUALSIGN_ID` | VARCHAR |  | The user who performed the second user verification on the immunization. |
| 38 | `IMMNZTN_DUALSIGN_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 39 | `IMM_DUALSIGNINSTANT_DTTM` | DATETIME (Local) |  | The instant at which this immunization was verified by the second user. |
| 40 | `IMMNZTN_DOSE_AMOUNT` | NUMERIC |  | Immunization dose amount. |
| 41 | `IMMNZTN_DOSE_UNIT_C_NAME` | VARCHAR | org | Immunization dose unit. |
| 42 | `IMM_DEL_REASON_C_NAME` | VARCHAR | org | Category value indicating the reason for deleting or canceling the immunization. |
| 43 | `IMM_SCANNED_BARCODE` | VARCHAR |  | The raw data captured during immunization barcode scanning. |
| 44 | `ENTRY_DTTM` | DATETIME (Local) |  | Contains the date and time that the immunization administration data was last updated. If the exact time is not known, a date may be contained in ENTRY_DATE instead. |
| 45 | `IMM_PRODUCT_C_NAME` | VARCHAR | org | The brand name associated with the vaccination administration, stored as a category value from a defined set of products. |
| 46 | `IMM_DEFER_DUR_C_NAME` | VARCHAR | org | Each category value represents a different time scale of deferral for a vaccine administration deferral (e.g. "brief", "permanent", etc...). This item does NOT store the specific length of time the vaccine was deferred. |
| 47 | `IMM_REG_STATUS_C_NAME` | VARCHAR |  | The current administration's overall status according to an external Immunization Registry. |
| 48 | `IMM_LST_REGINST_UTC_DTTM` | DATETIME (UTC) |  | Last instant in which the overall registry status from an Immunization Registry was updated for a vaccine administration problem list (LPL)record. |
| 49 | `IMM_MAR_ADM_INPATIENT_DATA_ID` | VARCHAR |  | Link to the INP record that may hold the administrations data. |
| 50 | `IMM_LOT_NUM_ID_LOT_NUM` | VARCHAR |  | The lot number on the vial for a given medication or immunization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `IMMUNZATN_ID` | [CLARITY_IMMUNZATN](CLARITY_IMMUNZATN.md) | sole_pk | high |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [IMMUNE_HISTORY](IMMUNE_HISTORY.md) | `IMMUNE_ID` | high |
| [IMM_HM_SEQ_NUM](IMM_HM_SEQ_NUM.md) | `IMMUNE_ID` | high |
| [PAT_IMMUNIZATIONS](PAT_IMMUNIZATIONS.md) | `IMMUNE_ID` | high |

