# AUDIOGRAM_DATA_TABLE

> Contains the values for sound sources, locations, frequencies, and thresholds documented when performing Audiogram exams.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (ID number) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOUND_SOURCE_C_NAME` | VARCHAR |  | The source the sound was generated from (Air Conduction, Mastoid Bone Conduction, etc.) during an Audiometry exam. |
| 4 | `SOUND_LOCATION_C_NAME` | VARCHAR |  | The location on the patient the sound is being heard from (Left Ear, Right Ear, Unknown) during an Audiometry exam. |
| 5 | `SOUND_FREQ_C_NAME` | VARCHAR |  | The frequency (in Hz) the sound was played at during an Audiometry exam. |
| 6 | `SOUND_THRESHOLD` | INTEGER |  | The lowest decibel at which the patient was able to hear the sound that was played during an Audiometry exam. |
| 7 | `NO_RESPONSE_YN` | VARCHAR |  | Whether or not the patient is able to hear the sound even if played at the highest decibel during an Audiometry exam. |
| 8 | `VIBROTACTILE_YN` | VARCHAR |  | The vibrotactile sensation is a phenomenon confounded with bone conducted sound through the skin |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

