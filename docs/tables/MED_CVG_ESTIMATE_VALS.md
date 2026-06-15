# MED_CVG_ESTIMATE_VALS

> This table holds information about values sent to the payer when generating a medication estimate.

**Primary key:** `MED_ESTIMATE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | Stores contact number. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `RESP_RESULT_C_NAME` | VARCHAR |  | Category value indicating the coverage query response result. |
| 8 | `EST_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 9 | `EST_QTY_UNIT_C_NAME` | VARCHAR | org | This item holds the category value indicating the unit of the dispense quantity used when generating this estimate. |
| 10 | `EST_DAYS_SUPPLY` | INTEGER |  | This item holds the days supply used when generating this estimate. |
| 11 | `EST_AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `EST_PHARM_ID` | NUMERIC |  | This item points to the pharmacy (PHR) record used for generating this estimate. |
| 13 | `EST_PHARM_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 14 | `EST_DAYS_SUPPLY_DEFAULT_YN` | VARCHAR |  | This item indicates if the days supply value used in this estimate was an estimate, instead of a calculation based on order details. |
| 15 | `EST_QUERY_REASON_C_NAME` | VARCHAR |  | This category indicates why a prescription benefit query was triggered. |
| 16 | `EST_QUANTITY` | NUMERIC |  | This item holds the dispense quantity used when generating this estimate. |
| 17 | `EST_QUERY_USER_ID` | VARCHAR |  | This item holds the ID of the user that initiated the RTPB query. |
| 18 | `EST_QUERY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `EST_DISP_INFO_EST_YN` | VARCHAR |  | When sending out an RTPB query, this item will be set to 1 if we are using an estimated dispense quantity / unit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_ESTIMATE_ID` | [MED_CVG_INFO](MED_CVG_INFO.md) | sole_pk | high |

