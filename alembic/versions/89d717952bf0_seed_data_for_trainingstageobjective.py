"""Seed data for TrainingStageObjective

Revision ID: 89d717952bf0
Revises: c2a97541dd16
Create Date: 2021-08-25 00:07:36.094683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89d717952bf0'
down_revision = 'c2a97541dd16'
branch_labels = None
depends_on = None


training_stage_objective_table = sa.table('training_stage_objective',
                                          sa.column('training_stage_objective_id', sa.Integer),
                                          sa.column('training_stage_key', sa.String(80)),
                                          sa.column('session_number', sa.Integer),
                                          sa.column('name', sa.String(120)),
                                          sa.column('description', sa.Text),
                                          sa.column('policy_reference', sa.String(100)),
                                          sa.column('policy_link', sa.Text),
                                          sa.column('display_order', sa.Integer())
                                          )

def upgrade():

    op.bulk_insert(training_stage_objective_table, [
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 1,
            'name': 'Review relevant sections of the 7110.65',
            'decription': '''2-1-1, 2-1-2, 2-1-4
                            2-4-3, 9, 15-22 
                            ''',
            'policy_reference': '7110.65',
            'policy_link': 'https://www.faa.gov/documentLibrary/media/Order/7110.65Y.pdf',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 1,
            'name': 'Learn how to use the CRAFT acronym effectively at PDX',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 2
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 1,
            'name': 'Discuss and review initial altitudes from the SOP',
            'decription': '',
            'policy_reference': 'SOP-102',
            'policy_link': '',
            'display_order': 3
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 1,
            'name': 'Practice amending flight plans',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 4
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 1,
            'name': 'Practice giving IFR clearances at PDX',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 5
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 2,
            'name': 'Discuss minor differences between IFR clearances at PDX vs VUO',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 2,
            'name': 'Initial Altitude for IFR departures out of VUO',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 2
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 2,
            'name': 'Explain what Hold for Release implies and why we use that phraseology',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 3
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 2,
            'name': 'Practice giving IFR clearances out of VUO',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 4
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 3,
            'name': 'Review and discuss VFR sections of the PDX SOP',
            'decription': 'SOP-102 sections 2.2.3 - 2.2.4',
            'policy_reference': 'SOP-102',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 3,
            'name': 'Review different types of airspace and their capabilities',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 2
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 3,
            'name': 'Discuss requirements for VFR aircraft to fly in the PDX Class C airspace',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 3
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 3,
            'name': 'Discuss and review relevant sections of the 7110.65',
            'decription': 'Sections 7-8-4 - 7-8-7',
            'policy_reference': '7110.65',
            'policy_link': 'https://www.faa.gov/documentLibrary/media/Order/7110.65Y.pdf',
            'display_order': 4
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 3,
            'name': 'Work a scenario with VFR aircraft',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 5
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Discuss and review PDX SOP section 2.3.1',
            'decription': '',
            'policy_reference': 'SOP-102 2.3.1',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Read and review the golden rules of ATC',
            'decription': 'Section 2-1-1 subpara a, b of 7110.65',
            'policy_reference': '711.65',
            'policy_link': 'https://www.faa.gov/documentLibrary/media/Order/7110.65Y.pdf',
            'display_order': 2
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Read and review relevant portions of the 7110.65',
            'decription': '',
            'policy_reference': '7110.65 3-7-2 - 3-7-3',
            'policy_link': 'https://www.faa.gov/documentLibrary/media/Order/7110.65Y.pdf',
            'display_order': 3
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Runway Crossing and intersection departure coordination.',
            'decription': '',
            'policy_reference': '7110.65 3-1-3',
            'policy_link': '',
            'display_order': 4
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Review items and errors to look for before taxiing an aircraft',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 5
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Practice moving aircraft at PDX in East Flow',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 6
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Practice moving aircraft at PDX in West Flow',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 7
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 4,
            'name': 'Practice moving aircraft at PDX in South Flow',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 8
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 5,
            'name': 'Read and discuss section 3-11-1 of the 7110.65',
            'decription': '',
            'policy_reference': '7110.65 Section 3-11-1',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 5,
            'name': 'Discuss the different types of helicopter taxi operations and how they differ',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 2
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 5,
            'name': 'Differences in responsibility between present position departure and active runway departure',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 3
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 5,
            'name': 'Practice all types of helicopter movements, and the associated phraseology',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 4
        },
        {
            'training_stage_key': 'MINOR_GROUND',
            'session_number': 6,
            'name': 'Practice all Delivery / Ground functions until you meet the competency requirements for S1',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MAJOR_GROUND',
            'session_number': 1,
            'name': 'Placeholder',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_TOWER',
            'session_number': 1,
            'name': 'Placeholder',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MAJOR_TOWER',
            'session_number': 1,
            'name': 'Placeholder',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MINOR_APPROACH',
            'session_number': 1,
            'name': 'Placeholder',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'MAJOR_APPROACH',
            'session_number': 1,
            'name': 'Placeholder',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },
        {
            'training_stage_key': 'CENTER',
            'session_number': 1,
            'name': 'Placeholder',
            'decription': '',
            'policy_reference': '',
            'policy_link': '',
            'display_order': 1
        },

    ])


def downgrade():
    op.execute('TRUNCATE TABLE training_stage_objective')
