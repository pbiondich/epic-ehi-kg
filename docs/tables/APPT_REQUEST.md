# APPT_REQUEST

> This table stores information about appointment requests.

**Primary key:** `REQUEST_ID`  
**Columns:** 12  
**Org-specific columns:** 1  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUEST_ID` | NUMERIC | PK | The unique identifier (.1 item) for the appointment request record. If the appointment request is also an order, this column can be joined to the ORDER_PROC_ID column in the ORDER_PROC tables. |
| 2 | `REQ_IS_ACCIDENT_YN` | VARCHAR |  | Indicates whether or not the reason for visit is related to an accident, workers' compensation, or other third party liability guarantor. |
| 3 | `REQ_SPECIAL_BILL_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 4 | `REQ_FIN_OUTPUT_ID` | VARCHAR |  | The unique ID of the Questionnaire Answers record that contains the results from running a Financial Decision Tree. |
| 5 | `REQ_FIN_SCREEN_DTTM` | DATETIME (Local) |  | The instant that the financial screening was last run on this order or appointment request. |
| 6 | `APPT_REQ_DECL_RSN_C_NAME` | VARCHAR | org | The reason provided by the patient for why they cancelled the scheduling ticket |
| 7 | `LINKED_SERIES_CSN_ID` | NUMERIC |  | If a recurring series of appointments was scheduled from this order, this item will contain the recur link (EPT 7150) of those appointments. |
| 8 | `PRIM_SPECIALTY_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 9 | `PRIM_SUBSPECIALTY_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 10 | `PRIM_CONDITION_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 11 | `PRIM_TREATMENT_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 12 | `PRIM_KEYWORD_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [APPT_REQ_RELEVANT_DEPTS](APPT_REQ_RELEVANT_DEPTS.md) | `REQUEST_ID` | high |
| [RXHI_DROP_SHIP_REQUESTS](RXHI_DROP_SHIP_REQUESTS.md) | `REQUEST_ID` | high |

