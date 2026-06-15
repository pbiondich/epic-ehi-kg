# EM_CODE_CALC

> Tracks Evaluation and Management (EM) code calculations based on LOS codes. EM codes are used by physicians to report and bill medical services depending on medical history, physical examinations and the level of medical decision making. This table also tracks the source of EM codes - if they were entered manually or via documentation.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the EM code associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EM_CODE_SECTION` | VARCHAR |  | The section of the patient's chart used to calculate the EM code. Ex: Review of Systems (ROS) or History of Present Illness (HPI) |
| 6 | `EM_CODE_ATTRIBUTE` | VARCHAR |  | The attribute of the section of the chart used to calculate the EM code. Ex: A Neuro or GI section in the Review of Systems (ROS) |
| 7 | `EMCODE_ASSO_NOTE_ID` | VARCHAR |  | Stores the note record ID corresponding to the note where this EM code was filed. |
| 8 | `EMCODE_SDI` | VARCHAR |  | This item stores the source SmartData Element Identifier (discrete piece of data) for the current line of EM code. |
| 9 | `EM_CODE_SOURCE_C_NAME` | VARCHAR |  | This item tracks if a particular EM Code was filed manually (not automatically via documentation) and which manual source filed this code. |
| 10 | `EM_CODE` | VARCHAR |  | The EM code value used to calculate level of service |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

