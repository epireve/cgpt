# Scope 1 - Direct emissions

Category for Scope 1 Activity:
- Stationary Combustion
- Mobile Sources
- Refrigeration & AC
- Fire Suppression
- Purchased gases

## Observation
Here are some observations and recommendations on optimizing this Scope 1 JSON schema:

**Structure**

- The top-level categories like "StationaryCombustion" nicely group related emissions sources. This organization is easy to understand.

- The structure with categories > sub-categories > fields makes sense for rendering forms.

- Consider flattening slightly by moving shared fields like "Date" up a level to reduce duplication.

**Data Patterns**

- Field names are descriptive (e.g. "Source Description"). Helps understandability.

- Reusing dropdown IDs (like "unitsDropdown") allows reusing options, good consistency.

- Disabling calculated emissions fields makes sense.

- Dropdown options are very extensive but repetitive.

**Improvements**

- Flatten structure slightly by moving common fields like Date/ID to category level to remove duplication.

- Reduce size by externalizing the many category/gas dropdown options into global lookup lists, referenced by ID instead of embedded.

- Use codes instead of descriptions where possible - e.g. "kg" vs "kilograms". Reduce size.

- Structure data hierarchically with foreign key relationships for more performant querying/aggregation.

- Add more semantic data types - e.g. use actual date vs text for dates. 

Overall the structure and naming make sense. Some tweaks as noted above around normalization and flattening would help optimize overall.



# Scope 2 - Indirect emissions

Category for Scope 2 Activity:
- Electricity
- Steam

## Observation

Here are some observations and suggestions on optimizing this Scope 2 JSON schema:

**Structure**

- The top-level "Electricity" and "Steam" categories group related emissions data nicely. Easy to understand structure.

- The nested structure with fields > sub-fields makes sense for rendering forms.

- Consider pulling shared fields like "Date" and "Source ID" up a level to avoid duplication.

**Data Patterns**  

- Field names are descriptive (e.g. "Source Description") which adds clarity.

- Reusing dropdown IDs enables reuse of options, allowing consistency.

- Disabling calculated emissions fields makes sense.

- Options around regions and fuels are very extensive but repetitive.

**Improvements**

- Flatten slightly by moving common fields like Date/ID to category level to reduce duplication.

- Reduce size by externalizing the extensive region and fuel type dropdown options into global lookup lists, referenced by ID instead of embedded.

- Use codes instead of descriptions where possible - e.g. "kWh" vs "kilowatt-hours". Reduces size.

- Structure data hierarchically with foreign key relationships to allow more performant querying/aggregation.  

- Add more semantic data types - e.g. actual dates instead of text for dates.

Overall the structure and naming patterns are understandable. Some tweaks like noted above around normalization and flattening would help optimize overall.




# Scope 3 - Indirect sources

Category for Scope 3 Activity, there are four categories:

A. Business Travel
B. Commuting
C. Upstream transport & Distance
D. Waste

Each of the categories has sub categories, except D. Waste:

A. Business Travel
- Personal Vehicle, Rental Car or Taxi
- Rail or Bus
- Air

B. Commuting
- Personal Vehicle
- Public Transportation

C. Upstream transport and distance
- Product Transport by Vehicle-Miles
- Product Transport by Ton-Miles

D. Waste

## Observation
Here are some observations and suggestions for optimizing this JSON schema:

**Structure**

- The overall structure with a top-level "Scope3Activity" object grouping related categories works well. This groups things neatly.

- The nesting with sub-categories is logical and easy to understand. For example, "Business Travel" has nicely grouped sub-categories.

- Using a "type: form" with a "fields" array for the categories creates a flexible data structure well suited for generating forms.

**Data Patterns**  

- There is some repetition in field names and structures across categories (e.g "Date", "Source ID"). Consider moving these common fields into the top category levels to reduce duplication.

- Field names and variables are descriptive which helps understandability.

- Re-using the same dropdown IDs (like "unitsDropdown") allows re-using options, good for consistency.

- Disabling emission fields that will be calculated makes sense.

**Improvements**

- Can flatten structure slightly moving common fields like dates and IDs to category level rather than sub-category level. Removes duplication.

- For reference data like vehicles and materials, normalize into global lookups that can be referenced by ID rather than embedding full dropdowns everywhere. Will reduce size.

- To optimize size:
  - Drop down options can be externalized into global lookup lists referenced by ID. Removes duplication.  
  - Where possible use codes instead of full text for IDs and keys (e.g. 1 instead of "kilometers")

- For computational performance, structure data hierarchically into relational datasets with foreign keys for efficient querying and aggregation.

Overall the structure, naming, and patterns make sense. Some minor tweaks as noted above could help improve size, performance and analytics capability.