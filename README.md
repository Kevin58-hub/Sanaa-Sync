# Sanaa-Sync
A Django-based ecosystem to digitize the Swahilipot Hub Creatives Department, moving from manual Google Drive/Physical filing to an automated, data-driven professional marketplace.
## Core User Roles (Permissions Logic)
Creative Admin (Dept. Head): Full oversight, booking approvals, duty roster management, and "Greenlighting" projects.

Creative (Artist): Profile management, multi-skill tagging, job application, and space/equipment booking.

Client/Partner: Posting gigs, viewing portfolios, and hiring talent.

Superuser (Dev Team): System maintenance.

## Functional Modules (The "App" Structure)

### The Artist Registry (Database & Portfolio)
Multi-Specialization Support: Allows artists to list multiple categories (Dancer, Poet, Model) to reflect their "varying arts" and career shifts.

Dynamic Profiles: Includes a "Success Stories" section and a "Sample Vetting" upload area for recruitment.

Availability Status: Real-time indicator: "Available for Hire" vs. "On a Project."

Artist History: A log of all past gigs and Hub-related activities to build credibility.

### Resource & Event Management (Booking System)
Asset Catalog: Digital tracking for the Amphitheatre, Mekatilili Hall, Ali Mazrui Hall, and equipment (Drums, Guitars, Mics).

The "Greenlight" Workflow: A digital request system that replaces verbal/email approvals. Requests stay "Pending" until the Dept. Head triggers an approval.

Events Calendar: A dual-view calendar showing Internal Hub Events vs. External Gigs.

Constraints Engine: Automated rules for "Early Booking" and "Max Usage Time" to prevent overbooking.

### The Marketplace & Gigs (Hiring Logic)
Job Board: Clients can upload job requirements; artists apply directly within the platform.

Vetting Pipeline: A workflow for poets/artists to send samples for department head review before they are recommended to partners.

Partner Network: A portal for "YouthHub Networks" and external partners to find verified talent.

### Internal Dept. Operations
Digital Duty Roster: Tracks which staff/interns are On-Duty, Off-Duty, or On Leave.

Activity Tracker: A "Live Now" section showing current rehearsals or events happening at the Hub.

## Technical Strategy 
User Profiles  - Use an AbstractUser with a ManyToManyField for Art Categories
Booking        - A Booking model with start_time, end_time, and a status ChoiceField. 
Availability   - A Boolean field is_hired that toogles based on active project links.
File Storage   - Move from Google Drive to Cloudinary or AWS S3 for artist samples.
UI/UX          - Tailwind CSS (Clean, "Swiss" style) to ensure artists take the tech seriously.


## Key Challenges & Goals to Solve
The "Pay Gap": By showcasing "Work Done Behind the Scenes" and "Success Stories," the platform aims to justify higher rates for artists.

Tech Integration: The platform itself is a teaching tool—it forces creatives to use tech (this app) to manage their art career.
