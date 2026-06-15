# MED_CVG_DETAILS

> This table holds details about medication coverages.

**Primary key:** `MED_ESTIMATE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PHR_TYPE_C_NAME` | VARCHAR |  | Holds the category value indicating the pharmacy type that is covered. |
| 6 | `DRUG_STATUS_C_NAME` | VARCHAR |  | Holds the category value of the drug coverage status. |
| 7 | `QTY_PRICED` | INTEGER |  | Holds the quantity priced. |
| 8 | `QTY_PRICED_UNIT_C_NAME` | VARCHAR | org | Holds the category value indicating the unit for the quantity priced. |
| 9 | `DAYS_SUPPLY` | INTEGER |  | Holds the days supply priced. |
| 10 | `PLAN_PAY_AMT` | NUMERIC |  | Holds the plan pay amount. |
| 11 | `PAT_PAY_AMT` | NUMERIC |  | Holds the estimated patient pay amount. |
| 12 | `OOP_APPLIED_AMT` | NUMERIC |  | Holds the out of pocket applied amount. |
| 13 | `OOP_REMAIN_AMT` | NUMERIC |  | Holds the out of pocket remaining amount. |
| 14 | `DEDUCT_APPLY_AMT` | NUMERIC |  | Holds the deductible applied amount. |
| 15 | `DEDUCT_REMAIN_AMT` | NUMERIC |  | Holds the deductible remaining amount. |
| 16 | `FORM_STATUS` | VARCHAR |  | Holds the formulary status. |
| 17 | `PA_REQ_C_NAME` | VARCHAR |  | Holds whether prior authorization is required for this medication. This is the effective prior authorization flag after considering system overrides. The actual value returned in the RTPB response is in item LME 322. |
| 18 | `PHARMACY_ID` | NUMERIC | FK→ | This item holds a pointer to the pharmacy (PHR) that was used for generating this estimate. |
| 19 | `PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 20 | `PRIMARY_CVG_YN` | VARCHAR |  | This item indicates if this line holds the coverage information that matches what was originally requested. |
| 21 | `DISPLAYED_BEFORE_SIGN_YN` | VARCHAR |  | This item indicates if this line of coverage data was displayed to an end-user before the order was signed. |
| 22 | `PREFERRED_PHARM_YN` | VARCHAR |  | Notes whether the alternative came from an RTPB preferred pharmacy as defined in the interface this alternative came from. |
| 23 | `RTPB_PA_REQ_C_NAME` | VARCHAR |  | Holds whether prior authorization is required for this medication. This is the actual value returned in the RTPB response. Item LME 316 holds the effective prior authorization flag after considering system overrides. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_ESTIMATE_ID` | [MED_CVG_INFO](MED_CVG_INFO.md) | sole_pk | high |
| `PHARMACY_ID` | [RX_PHR](RX_PHR.md) | sole_pk | high |

