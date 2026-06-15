# INTVTN_CONTACT

> The INTVTN_CONTACT table contains information about care plan intervention records. This information includes the unique ID of the intervention, its frequency, and data on edits made.

**Primary key:** `INTERVENTION_ID`, `CONTACT_DATE_REAL`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | The unique ID of the intervention record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_TYPE_C_NAME` | VARCHAR |  | The contact type category ID for this intervention. This column is commonly used to differentiate edits from documentation instances. |
| 5 | `EDIT_INSTANT_DTTM` | DATETIME (Local) |  | The date and time the intervention was last edited. |
| 6 | `EDIT_USER_ID` | VARCHAR |  | The unique ID associated with the user who edited the care plan intervention data. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `SCHEDULED_VISITS` | VARCHAR |  | Care plan intervention scheduled visits. |
| 9 | `CARE_PLAN_CSN` | VARCHAR |  | The link to the unique contact serial number for this care plan contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). This column is used to recreate historic versions of a care plan. |
| 10 | `PAT_CSN` | NUMERIC | FK→ | Stores the visit this intervention documentation event was done in. |
| 11 | `HAS_NOTE_EDIT_YN` | VARCHAR |  | Y means that, for this reading, the default smarttext has been pulled in at least once. |
| 12 | `READING_UTC_DTTM` | DATETIME (UTC) |  | Documents when the original reading contact was documented. Used to order active documentation readings in the order they clinically happened. |
| 13 | `NAME_DISPLAY` | VARCHAR |  | The display name of the intervention. |
| 14 | `UPDATED_INTERVENTION_ID` | VARCHAR |  | This item links to the newly created intervention ID that was made when this original intervention was completed and updated. |
| 15 | `REASON_FOR_UPDATE` | VARCHAR |  | Contains the reason as to why this element was resolved and updated. |
| 16 | `INTV_RESPONSIBLE_USER_ID` | VARCHAR |  | The responsible user for the intervention. |
| 17 | `INTV_RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `INTV_RESPONSIBLE_IB_POOL_ID` | NUMERIC |  | The responsible pool for the intervention. |
| 19 | `INTV_RESPONSIBLE_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 20 | `LINKED_EPISODE_ID` | NUMERIC |  | Stores the episode associated with the intervention's care plan. |
| 21 | `FREQ_OVRD_DAY_TYPE` | INTEGER |  | Specifies what the numeric values in the frequency override days (I LPI 34655) represent. Currently this is always set to 1, which means that the values listed in I LPI 34655 are days relative to the start date of the recurrence. |
| 22 | `FREQ_OVRD_CYCLE_LENGTH` | INTEGER |  | If there is a frequency override specified, this item will contain the length of a relative specified type cycle. For all other specified types this value will be ignored (and should be empty). |
| 23 | `TREATMENT_CLASS_ID` | NUMERIC | FK→ | The treatment class this reading was documented under (users can change treatment classes for a specific activity). |
| 24 | `TREATMENT_CLASS_ID_DISPLAY_NAME` | VARCHAR |  | The name of the treatment class that is displayed to end users. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `TREATMENT_CLASS_ID` | [TREATMENT_CLASS](TREATMENT_CLASS.md) | sole_pk | high |

