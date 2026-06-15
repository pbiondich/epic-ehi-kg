# PROBLEM_LIST_HX

> This table contains data relating to the history of problems from patients' problem lists in the clinical system.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique ID of this Problem List entry. |
| 2 | `LINE` | INTEGER | PK | Used to identify the particular problem within the historical problems |
| 3 | `HX_PROBLEM_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `HX_DESCRIPTION` | VARCHAR |  | The historical display name of the problem. Only contains data if the default display name is changed. |
| 5 | `HX_DATE_NOTED` | DATETIME |  | Represents the historical value of the first possible date that a problem could have been noted/onset on. A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the earliest date of the effective range. See HX_NOTED_END_DATE for the latest counterpart. For example, if 2012 is documented in hyperspace, then HX_NOTED_DATE will be 1/1/2012 and HX_NOTED_END_DATE will be 12/31/2012. |
| 6 | `HX_DATE_RESOLVED` | DATETIME |  | The date on which this problem was resolved. |
| 7 | `HX_COMMENT` | VARCHAR |  | The historical preview text (first characters) of all the Overview notes entered for a Problem List entry. |
| 8 | `HX_DATE_OF_ENTRY` | DATETIME |  | The date that the problem was added to or updated on the patient's Problem List in calendar format. |
| 9 | `HX_ENTRY_USER_ID` | VARCHAR |  | The ID of the user who edited this problem on the patient's Problem List. This ID may be encrypted. |
| 10 | `HX_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `HX_MYCHART_YN` | VARCHAR |  | Indicates this problem was visible on web based chart system when this historical action was recorded. |
| 12 | `HX_CHRONIC_YN` | VARCHAR |  | This column indicates whether or not this problem was flagged as chronic as of this historical event. |
| 13 | `HX_PRINCIPAL_YN` | VARCHAR |  | This column indicates whether or not this problem was flagged as the principal problem as of this historical event. |
| 14 | `HX_IS_HOSP_YN` | VARCHAR |  | This column indicates whether or not this problem was flagged as a hospital problem as of this historical event. |
| 15 | `HX_PROBLEM_EPT_CSN` | NUMERIC |  | Contact Serial Number (CSN) of the patient encounter where this historical problem list was documented. |
| 16 | `HX_STATUS_C_NAME` | VARCHAR |  | The category value associated with the problem's state: Active, Resolved, or Deleted as of this historical event. |
| 17 | `HX_LEVEL_URGENCY_C_NAME` | VARCHAR | org | The category value associated with the level of urgency of the problem at the time this history event was recorded. |
| 18 | `HX_PRIORITY_C_NAME` | VARCHAR | org | The category value associated with the relative severity of the problem. Problems can be given a priority (e.g., "high, medium, or low" ). This field shows the category value associated with the priority level assigned to a problem when this action was taken. |
| 19 | `HX_ENTRY_INST` | DATETIME (Local) |  | The date and time when the problem was updated on the patient's problem list. |
| 20 | `HX_PROBLEM_POA_C_NAME` | VARCHAR | org | This column has the history of the present on admission indicator, which indicates if a hospital problem was present on admission or not. |
| 21 | `HX_STAGE_ID` | NUMERIC |  | This column holds the history of all stages ever associated with this problem. |
| 22 | `HX_NOTED_END_DATE` | DATETIME |  | Represents the historical value of the last possible date that a problem could have been noted/onset on. A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the latest date of the effective range. See HX_NOTED_DATE for the latest counterpart. For example, if 2012 is documented in hyperspace, then HX_NOTED_DATE will be 1/1/2012 and HX_NOTED_END_DATE will be 12/31/2012. Note that the value may be empty, even if HX_NOTED_DATE is populated |
| 23 | `HX_DIAG_START_DATE` | DATETIME |  | Represents the earliest possible date that a problem could have been diagnosed on at a particular edit. The latest possible date is stored in HX_DIAG_END_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |
| 24 | `HX_DIAG_END_DATE` | DATETIME |  | Represents the last possible date that a problem could have been diagnosed on at a particular edit. The earliest possible date is stored in HX_DIAG_START_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

