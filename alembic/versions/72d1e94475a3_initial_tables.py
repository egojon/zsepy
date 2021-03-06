"""Initial Tables

Revision ID: 72d1e94475a3
Revises: 
Create Date: 2021-08-25 00:06:48.518493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d1e94475a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airport',
    sa.Column('airport_icao', sa.String(length=4), nullable=False),
    sa.Column('name', sa.String(length=240), nullable=True),
    sa.Column('facility', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('airport_icao')
    )
    op.create_table('airport_arrival',
    sa.Column('airport_icao', sa.String(length=4), nullable=False),
    sa.Column('name', sa.String(length=6), nullable=False),
    sa.PrimaryKeyConstraint('airport_icao', 'name')
    )
    op.create_table('airport_departure',
    sa.Column('airport_icao', sa.String(length=4), nullable=False),
    sa.Column('name', sa.String(length=6), nullable=False),
    sa.Column('departure_type', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('airport_icao', 'name')
    )
    op.create_table('airport_runway',
    sa.Column('airport_icao', sa.String(length=4), nullable=False),
    sa.Column('code', sa.String(length=3), nullable=False),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('airport_icao', 'code')
    )
    op.create_table('controller',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('initials', sa.String(length=4), nullable=True),
    sa.Column('rating', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('display_name', sa.String(length=240), nullable=True),
    sa.Column('email_address', sa.String(length=240), nullable=True),
    sa.Column('member_since', sa.Date(), nullable=True),
    sa.Column('facility', sa.String(length=20), nullable=True),
    sa.Column('is_home', sa.Boolean(), nullable=True),
    sa.Column('is_visitor', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('vatsim_cid'),
    sa.UniqueConstraint('initials')
    )
    op.create_table('controller_document_read',
    sa.Column('vatsim_cid', sa.Integer(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.Column('first_read', sa.DateTime(), nullable=True),
    sa.Column('last_read', sa.DateTime(), nullable=True),
    sa.Column('is_latest_version_read', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('vatsim_cid', 'document_id')
    )
    op.create_table('controller_profile',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('timezone', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('vatsim_cid')
    )
    op.create_table('document',
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.Column('document_category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('google_document_id', sa.String(length=240), nullable=True),
    sa.Column('created_by_cid', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_by_cid', sa.Integer(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('document_id')
    )
    op.create_table('document_category',
    sa.Column('document_category_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('is_public', sa.Boolean(), nullable=True),
    sa.Column('show_instructor', sa.Boolean(), nullable=True),
    sa.Column('show_mentor', sa.Boolean(), nullable=True),
    sa.Column('show_staff', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('document_category_id')
    )
    op.create_table('email_template',
    sa.Column('template_id', sa.String(length=240), nullable=False),
    sa.Column('template_name', sa.String(length=240), nullable=False),
    sa.Column('additional_cc_list', sa.Text(), nullable=False),
    sa.Column('content_plaintext', sa.Text(), nullable=False),
    sa.Column('content_html', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('template_id')
    )
    op.create_table('external_link',
    sa.Column('external_link_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=240), nullable=False),
    sa.Column('link', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('external_link_id')
    )
    op.create_table('news',
    sa.Column('news_id', sa.Integer(), nullable=False),
    sa.Column('poster_cid', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=240), nullable=False),
    sa.Column('link', sa.Text(), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('news_id')
    )
    op.create_table('notam',
    sa.Column('notam_id', sa.Integer(), nullable=False),
    sa.Column('poster_cid', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=240), nullable=False),
    sa.Column('link', sa.Text(), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('notam_id')
    )
    op.create_table('preferred_route',
    sa.Column('departure_airport', sa.String(length=4), nullable=False),
    sa.Column('arrival_airport', sa.String(length=4), nullable=False),
    sa.Column('route', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('departure_airport', 'arrival_airport')
    )
    op.create_table('training_stage',
    sa.Column('training_stage_key', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('required_rating', sa.String(length=80), nullable=False),
    sa.Column('is_visitor_path', sa.Boolean(), nullable=False),
    sa.Column('is_home_path', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('training_stage_key')
    )
    op.create_table('controller_discord',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('discord_id', sa.String(length=40), nullable=False),
    sa.Column('notifications', sa.Boolean(), nullable=True),
    sa.Column('on_voice_channel', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['vatsim_cid'], ['controller.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('vatsim_cid'),
    sa.UniqueConstraint('discord_id')
    )
    op.create_table('controller_inactivity',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('is_inactivity_exempt', sa.Boolean(), nullable=True),
    sa.Column('inactivity_strikes', sa.Integer(), nullable=True),
    sa.Column('inactivity_start', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['vatsim_cid'], ['controller.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('vatsim_cid')
    )
    op.create_table('controller_loa',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('reason', sa.String(length=240), nullable=True),
    sa.Column('request_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['vatsim_cid'], ['controller.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('vatsim_cid')
    )
    op.create_table('controller_log',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('controller_cid', sa.Integer(), nullable=False),
    sa.Column('admin_cid', sa.Integer(), nullable=True),
    sa.Column('log_date', sa.DateTime(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['controller_cid'], ['controller.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('controller_positions',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('delivery', sa.String(length=80), nullable=True),
    sa.Column('ground', sa.String(length=80), nullable=True),
    sa.Column('tower', sa.String(length=80), nullable=True),
    sa.Column('approach', sa.String(length=80), nullable=True),
    sa.Column('center', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['vatsim_cid'], ['controller.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('vatsim_cid')
    )
    op.create_table('controller_training_stage',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('training_stage_key', sa.String(length=80), autoincrement=False, nullable=False),
    sa.Column('is_allowed_to_train', sa.Boolean(), nullable=False),
    sa.Column('requirements_completed_date', sa.DateTime(), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.Column('completed_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['training_stage_key'], ['training_stage.training_stage_key'], ),
    sa.PrimaryKeyConstraint('vatsim_cid', 'training_stage_key')
    )
    op.create_table('staff',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('staff_position', sa.String(length=80), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_mentor', sa.Boolean(), nullable=False),
    sa.Column('is_instructor', sa.Boolean(), nullable=False),
    sa.Column('is_training_administrator', sa.Boolean(), nullable=False),
    sa.Column('is_facility_engineer', sa.Boolean(), nullable=False),
    sa.Column('is_event_coordinator', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['vatsim_cid'], ['controller.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('vatsim_cid')
    )
    op.create_table('training_session',
    sa.Column('training_session_id', sa.Integer(), nullable=False),
    sa.Column('student_cid', sa.Integer(), nullable=False),
    sa.Column('instructor_cid', sa.Integer(), nullable=False),
    sa.Column('training_type', sa.String(length=80), nullable=False),
    sa.Column('training_stage_key', sa.String(length=80), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comments', sa.String(length=240), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('movements', sa.Integer(), nullable=False),
    sa.Column('is_private', sa.Boolean(), nullable=False),
    sa.Column('is_ots_ready', sa.Boolean(), nullable=False),
    sa.Column('is_pass', sa.Boolean(), nullable=True),
    sa.Column('session_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['training_stage_key'], ['training_stage.training_stage_key'], ),
    sa.PrimaryKeyConstraint('training_session_id')
    )
    op.create_table('training_stage_objective',
    sa.Column('training_stage_objective_id', sa.Integer(), nullable=False),
    sa.Column('training_stage_key', sa.String(length=80), nullable=False),
    sa.Column('session_number', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=240), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('policy_reference', sa.String(length=100), nullable=True),
    sa.Column('policy_link', sa.Text(), nullable=True),
    sa.Column('display_order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['training_stage_key'], ['training_stage.training_stage_key'], ),
    sa.PrimaryKeyConstraint('training_stage_objective_id')
    )
    op.create_table('training_stage_requirement',
    sa.Column('training_stage_requirement_id', sa.Integer(), nullable=False),
    sa.Column('training_stage_key', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=240), nullable=False),
    sa.Column('requirement_type', sa.String(length=80), nullable=False),
    sa.Column('reference_id', sa.Integer(), nullable=True),
    sa.Column('reference_value', sa.String(length=240), nullable=True),
    sa.ForeignKeyConstraint(['training_stage_key'], ['training_stage.training_stage_key'], ),
    sa.PrimaryKeyConstraint('training_stage_requirement_id')
    )
    op.create_table('controller_training_stage_requirement',
    sa.Column('vatsim_cid', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('training_stage_requirement_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.Column('completed_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['training_stage_requirement_id'], ['training_stage_requirement.training_stage_requirement_id'], ),
    sa.ForeignKeyConstraint(['vatsim_cid'], ['controller_training_stage.vatsim_cid'], ),
    sa.PrimaryKeyConstraint('vatsim_cid', 'training_stage_requirement_id')
    )
    op.create_table('training_request',
    sa.Column('training_request_id', sa.Integer(), nullable=False),
    sa.Column('student_cid', sa.Integer(), nullable=False),
    sa.Column('training_stage_key', sa.String(length=80), nullable=False),
    sa.Column('window_start_date', sa.DateTime(), nullable=False),
    sa.Column('window_end_date', sa.DateTime(), nullable=False),
    sa.Column('is_accepted', sa.Boolean(), nullable=False),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.Column('is_cancelled', sa.Boolean(), nullable=False),
    sa.Column('instructor_cid', sa.Integer(), nullable=True),
    sa.Column('training_session_id', sa.Integer(), nullable=True),
    sa.Column('scheduled_start_date', sa.DateTime(), nullable=True),
    sa.Column('scheduled_end_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['instructor_cid'], ['controller.vatsim_cid'], ),
    sa.ForeignKeyConstraint(['student_cid'], ['controller.vatsim_cid'], ),
    sa.ForeignKeyConstraint(['training_session_id'], ['training_session.training_session_id'], ),
    sa.ForeignKeyConstraint(['training_stage_key'], ['training_stage.training_stage_key'], ),
    sa.PrimaryKeyConstraint('training_request_id')
    )
    op.create_table('training_session_objective',
    sa.Column('training_session_objective_id', sa.Integer(), nullable=False),
    sa.Column('training_session_id', sa.Integer(), nullable=False),
    sa.Column('training_stage_objective_id', sa.Integer(), nullable=False),
    sa.Column('is_lecture', sa.Boolean(), nullable=True),
    sa.Column('is_observed', sa.Boolean(), nullable=True),
    sa.Column('is_focus_area', sa.Boolean(), nullable=True),
    sa.Column('is_complete', sa.Boolean(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['training_stage_objective_id'], ['training_stage_objective.training_stage_objective_id'], ),
    sa.PrimaryKeyConstraint('training_session_objective_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('training_session_objective')
    op.drop_table('training_request')
    op.drop_table('controller_training_stage_requirement')
    op.drop_table('training_stage_requirement')
    op.drop_table('training_stage_objective')
    op.drop_table('training_session')
    op.drop_table('staff')
    op.drop_table('controller_training_stage')
    op.drop_table('controller_positions')
    op.drop_table('controller_log')
    op.drop_table('controller_loa')
    op.drop_table('controller_inactivity')
    op.drop_table('controller_discord')
    op.drop_table('training_stage')
    op.drop_table('preferred_route')
    op.drop_table('notam')
    op.drop_table('news')
    op.drop_table('external_link')
    op.drop_table('email_template')
    op.drop_table('document_category')
    op.drop_table('document')
    op.drop_table('controller_profile')
    op.drop_table('controller_document_read')
    op.drop_table('controller')
    op.drop_table('airport_runway')
    op.drop_table('airport_departure')
    op.drop_table('airport_arrival')
    op.drop_table('airport')
    # ### end Alembic commands ###
