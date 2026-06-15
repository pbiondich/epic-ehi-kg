# V_EHI_ICF_CYCLE_PATIENTS_DATA

> The INFERTILITY_CYCLE_LINKS table is not able to safely export all of its columns without potentially compromising the other patients that are attached to the infertility treatment cycle. The extracted patient's roles (e.g., sperm donor, intended parent) on the infertility treatment cycle determines the data they are allowed to view about the other patients attached to the cycle. This view filters the full data of the INFERTILITY_CYCLE_LINKS table based on the extracted patient's roles to be safely exported without compromising PHI. All extracted patients should be able to see the type of roles that were a part of a cycle (e.g., there is a sperm provider). Extracted patients with the role of intended parent should be able to see all the name of the known donors and the external donor information. Extracted patients with the role of known donor (a non-anonymous sperm or egg provider but not an intended parent) should be able to see all the names of the other known donors and intended parents but not the external donor information. Extracted patients with the role of anonymous donor should not be able to see any of the names of the other patients on the cycle or the external donor information.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier for the fertility treatment cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_PAT_ID` | VARCHAR | FK→ | The patient ID of a patient involved in a fertility treatment cycle. |
| 4 | `PAT_NAME` | VARCHAR |  | The patient’s name in the format Lastname, Firstname MI. |
| 5 | `IS_EXTRACTED_PAT_YN` | VARCHAR |  | When extracting a patient's cycles, rows marked with 'Y' represent their roles on the cycle. Else if marked 'N' then that row represents another patient attached to the cycle. The extracted patient refers to the LINKED_PAT_ID column. |
| 6 | `DONOR_DONATION_AGE` | INTEGER |  | The age of the donor at the time of donation of the specimen (sperm or egg). |
| 7 | `DONOR_DONATION_DATE` | DATETIME |  | The date of donation of the specimen (sperm or egg). |
| 8 | `DONOR_BANK` | VARCHAR |  | The name of the donation bank the specimen had came from. |
| 9 | `DONOR_BANK_CMT` | VARCHAR |  | A free text comment for the name of the donation bank. |
| 10 | `DONOR_GAMETE_ID` | VARCHAR |  | The gamete donor ID (may be assigned by the donation bank). |
| 11 | `DONOR_RACE` | VARCHAR |  | A patient's race. Multiple races may be associated with this patient. This is represented by a semicolon (;) delimited string. The values in this column come from the TITLE column of the ZC_PATIENT_RACE table. |
| 12 | `DONOR_RELATIONSHIP_C_NAME` | VARCHAR | org | This column indicates the type of relationship of the external donor to the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |
| `LINKED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

