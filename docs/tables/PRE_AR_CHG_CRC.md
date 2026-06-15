# PRE_AR_CHG_CRC

> This table holds the CRC information for a given charge line of a single transaction record. CRC stands for Condition Indicator, and in this case it is specifically vision-related CRC. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `CHARGE_LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `CHARGE_LINE` | INTEGER | PK | The line number for the information associated with this transaction record. This represents a single charge procedure in the transaction. |
| 3 | `CODE_C` | INTEGER |  | What sort of vision-related hardware was given. 1 = E1 - Spectacle Lenses 2 = E2 - Contact Lenses 3 = E3 - Spectacle Frames |
| 4 | `CONDITION_1_C` | INTEGER |  | The condition indicator code category ID. 1 = L1 - General Standard of 20 Degree or .5 Diopter Sphere or Cylinder Change Met 2 = L2 - Replacement Due to Loss or Theft 3 = L3 - Replacement Due to Breakage or Damage. |
| 5 | `CONDITION_2_C` | INTEGER |  | The condition indicator code category ID. 1 = L1 - General Standard of 20 Degree or .5 Diopter Sphere or Cylinder Change Met 2 = L2 - Replacement Due to Loss or Theft 3 = L3 - Replacement Due to Breakage or Damage. |
| 6 | `CONDITION_3_C` | INTEGER |  | The condition indicator code category ID. 1 = L1 - General Standard of 20 Degree or .5 Diopter Sphere or Cylinder Change Met 2 = L2 - Replacement Due to Loss or Theft 3 = L3 - Replacement Due to Breakage or Damage. |
| 7 | `CONDITION_4_C` | INTEGER |  | The condition indicator code category ID. 1 = L1 - General Standard of 20 Degree or .5 Diopter Sphere or Cylinder Change Met 2 = L2 - Replacement Due to Loss or Theft 3 = L3 - Replacement Due to Breakage or Damage. |
| 8 | `CONDITION_5_C` | INTEGER |  | The condition indicator code category ID. 1 = L1 - General Standard of 20 Degree or .5 Diopter Sphere or Cylinder Change Met 2 = L2 - Replacement Due to Loss or Theft 3 = L3 - Replacement Due to Breakage or Damage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

