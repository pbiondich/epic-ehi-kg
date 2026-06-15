# TIMEOUT_ABO_INFO

> ABO blood type verification information for the timeout.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the timeout record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DONOR_ABO_C_NAME` | VARCHAR |  | Stores the donor blood group. |
| 6 | `DONOR_ABO_M_YN` | VARCHAR |  | Stores whether the donor blood group in the timeout record matches the donor blood group value recorded in the organ record |
| 7 | `DNR_UNOSID` | VARCHAR |  | Stores the Donor ID from the United Network for Organ Sharing (UNOS) for the timeout record |
| 8 | `DNR_UNOS_ID_M_YN` | VARCHAR |  | Stores whether the donor's United Network for Organ Sharing (UNOS) ID in the timeout record matches the donor UNOS ID value recorded in the organ record |
| 9 | `ORGAN_ID` | NUMERIC |  | Stores the organ ID referenced for the donor blood group and donor's United Network for Organ Sharing (UNOS) ID |
| 10 | `ABO_PROC_ID` | VARCHAR |  | Stores the procedure that the blood group information relates to. |
| 11 | `ABO_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 12 | `ABO_COMPATIBLE_YN` | VARCHAR |  | Stores if the blood groups were recorded as compatible. |
| 13 | `ABO_INCOMPATIBL_CMT` | VARCHAR |  | The reason the procedure was performed in spite of blood group incompatibility. |
| 14 | `ORGAN_VERIFIED_C_NAME` | VARCHAR |  | Indicates the type of organ this blood group verification entry is for. Primarily used when dealing with transplants that have no organ records attached. |
| 15 | `RECIPIENT_NAME_MRN` | VARCHAR |  | The name and medical record number of the intended recipient for a living donor transplant procedure. |
| 16 | `RECIPIENT_ABO_C_NAME` | VARCHAR |  | The blood group of the intended recipient for a living donor transplant procedure. |
| 17 | `RECIP_VERIFIED_YN` | VARCHAR |  | Indicates whether the recipient identity pulled in from the organ link was verified. |
| 18 | `REC_ABO_VERIFIED_YN` | VARCHAR |  | Indicates whether the recipient blood group pulled in from the organ link was verified. |
| 19 | `VEL_ID` | NUMERIC |  | Stores the anatomy record ID entered during organ check-in |
| 20 | `VEL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 21 | `ABO_INCOMPAT_RSN_C_NAME` | VARCHAR | org | Indicates the reason they are proceeding with an ABO incompatibly transplant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

