# RX_MED_TRANSITION

> Table for information about medication transitions functionality available in outpatient pharmacy. One record in this table corresponds to one pharmacy system-level initiative to transition patients to a new medication, or to have their medication changed in some clinically significant way. One such record is stored in the LFT masterfile, and contains data such as a description of the system-level initiative, as well as instructions intended for ambulatory pharmacy users that might encounter medications marked with this medication transition data.

**Primary key:** `FOLLOW_UP_1_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FOLLOW_UP_1_ID` | NUMERIC | PK | The unique identifier (.1 item) for the tracking record. |
| 2 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 3 | `DESCRIPTION` | VARCHAR |  | This item stores a description of the medication transition represented by the LFT record. |
| 4 | `INSTRUCTIONS` | VARCHAR |  | This item stores the instructions displayed to ambulatory pharmacy system users when they are informed that a prescription identified by its linkage to this LFT record is to be transitioned to a different medication. |
| 5 | `CREATING_USER_ID` | VARCHAR |  | This item stores the user that created the medication transition LFT record. |
| 6 | `CREATING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `FLG_FILLS_IN_PROGRESS_YN` | VARCHAR |  | This item determines whether associating prescriptions with a medication transition should flag fills in progress. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

