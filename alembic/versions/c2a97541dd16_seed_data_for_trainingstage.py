"""Seed data for TrainingStage

Revision ID: c2a97541dd16
Revises: 72d1e94475a3
Create Date: 2021-08-25 00:07:21.107868

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c2a97541dd16'
down_revision = '72d1e94475a3'
branch_labels = None
depends_on = None

training_stage_table = sa.table('training_stage',
                                sa.column('training_stage_key', sa.String(80)),
                                sa.column('name', sa.String(120)),
                                sa.column('required_rating', sa.Enum),
                                sa.column('is_visitor_path', sa.Boolean),
                                sa.column('is_home_path', sa.Boolean)
                                )


def upgrade():
    op.bulk_insert(training_stage_table, [
        {'training_stage_key': 'MINOR_GROUND', 'name': 'Minor Ground', 'required_rating': 'OBS',
         'is_visitor_path': False, 'is_home_path': True},
        {'training_stage_key': 'MAJOR_GROUND', 'name': 'Major Ground', 'required_rating': 'S1',
         'is_visitor_path': False, 'is_home_path': True},
        {'training_stage_key': 'MINOR_TOWER', 'name': 'Minor Tower', 'required_rating': 'S1',
         'is_visitor_path': False, 'is_home_path': True},
        {'training_stage_key': 'MAJOR_TOWER', 'name': 'Major Tower', 'required_rating': 'S2',
         'is_visitor_path': False, 'is_home_path': True},
        {'training_stage_key': 'MINOR_APPROACH', 'name': 'Minor Approach', 'required_rating': 'S2',
         'is_visitor_path': False, 'is_home_path': True},
        {'training_stage_key': 'MAJOR_APPROACH', 'name': 'Major Approach', 'required_rating': 'S3',
         'is_visitor_path': False, 'is_home_path': True},
        {'training_stage_key': 'CENTER', 'name': 'Center', 'required_rating': 'S3',
         'is_visitor_path': False, 'is_home_path': True},
    ])
    pass


def downgrade():
    op.execute('TRUNCATE TABLE training_stage')
