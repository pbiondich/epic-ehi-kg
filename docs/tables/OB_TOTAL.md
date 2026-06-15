# OB_TOTAL

> This patient information table holds the obstetrics information for each patient history contact. The table contains information on multiple births, induced abortions, spontaneous abortions, ectopics, molars, gravidity, parity, abortions, related comments, full-term, premature, living, and live births. These values are all running totals across the patient's lifetime, calculated at the time of the history contact.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | Contact serial number is unique across all patients and all contacts |
| 2 | `OB_MULTIPLE_BIRTHS` | INTEGER |  | This column holds the number of multiple births. |
| 3 | `OB_THERAPEUTIC_AB` | INTEGER |  | This column holds the number of induced abortions. Along with values in columns OB_SPONTANEOUS_AB and OB_ECTOPICS comprise OB_ABORTIONS. |
| 4 | `OB_SPONTANEOUS_AB` | INTEGER |  | This column holds the number of spontaneous abortions. Along with the value in OB_THERAPEUTIC_AB and OB_ECTOPICS, comprise OB_ABORTIONS. |
| 5 | `OB_ECTOPICS` | INTEGER |  | This column holds the number of ectopic pregnancies. This number is included with the values in column OB_THERAPEUTIC_AB and OB_SPONTANEOUS_AB to calculate the value in OB_ABORTIONS. |
| 6 | `OB_GRAVIDITY` | VARCHAR |  | This column holds the number of total pregnancies for a patient. This column is the sum of the values in columns OB_PARITY and OB_ABORTIONS. |
| 7 | `OB_PARITY` | VARCHAR |  | The column contains information regarding how many pregnancies the patient carried past a gestational age (GA) of 24 weeks. The value in this column, along with the value in OB_ABORTIONS, comprises OB_GRAVIDITY. |
| 8 | `OB_ABORTIONS` | VARCHAR |  | This item is used to comment on obstetrics abortions reported at each contact. This column along with value in column OB_PARITY, makes up column OB_GRAVIDITY. This item is the sum total of columns OB_THERAPEUTIC_AB, OB_SPONTANEOUS_AB, OB_ECTOPICS. |
| 9 | `OB_COMMENT` | VARCHAR |  | This holds general comments for the patient's obstetric history. |
| 10 | `OB_FULL_TERM` | VARCHAR |  | This holds the number of full term pregnancies for a patient. Along with the value in column OB_PREMATURE, sums to the value in column OB_PARITY. |
| 11 | `OB_PREMATURE` | VARCHAR |  | This items holds the number of pregnancies which ended at a premature gestational age (GA). Along with column OB_FULL_TERM, sums to OB_PARITY. |
| 12 | `OB_LIVING` | VARCHAR |  | This item holds the number of the patient's currently living children as documented in the obstetric history. |
| 13 | `OB_PREG_HX_C_NAME` | VARCHAR |  | This column indicates whether the patient has a history of pregnancy, or if they have not been asked. It uses category values 1, 2, and 3, which represent the string values, 'Yes', 'No', and 'Not asked' respectively. These string values can be found by linking to table ZC_OB_PREG_HX. |
| 14 | `OB_LIVE_BIRTHS` | VARCHAR |  | A count of the number of children born alive for a patient. |
| 15 | `OB_MOLAR` | VARCHAR |  | The number of molar pregnancies the patient has had. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

