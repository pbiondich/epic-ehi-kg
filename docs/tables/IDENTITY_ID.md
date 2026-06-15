# IDENTITY_ID

> The IDENTITY_ID table contains the system master person index ID numbers for your patients. Each patient may have multiple master person index IDs; therefore, a line number is used to identify each identification number for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record internally and links to the patient table. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number of the patient ID within the patient’s record. |
| 3 | `IDENTITY_ID` | VARCHAR |  | The identification number associated with the patient. This ID may be encrypted. NOTE: This is the identification number that corresponds to the IDENTITY_TYPE_ID column listed in this same record. |
| 4 | `IDENTITY_TYPE_ID` | NUMERIC |  | The system master person index ID type corresponding to this identification number for the patient. Master person index distinguishes ID numbers from different locations and service areas based on their type. Type can also be used to designate non-system IDs to be populated and used to interface with data from other systems. |
| 5 | `IDENTITY_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

