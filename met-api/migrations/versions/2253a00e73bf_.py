"""

Revision ID: 2253a00e73bf
Revises: cad222167ce7
Create Date: 2023-02-06 10:57:24.811178

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2253a00e73bf'
down_revision = 'cad222167ce7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('UPDATE comment SET created_date = CURRENT_TIMESTAMP  WHERE created_date IS NULL;')
    op.alter_column('comment', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('comment_status', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('comment_status', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.alter_column('comment_status', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('contact', 'updated_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('contact', 'created_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('contact', 'updated_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('email_verification', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('engagement_status', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('engagement_status', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.alter_column('engagement_status', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('feedback', sa.Column('updated_date', sa.DateTime(), nullable=True))
    op.add_column('feedback', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('feedback', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.alter_column('feedback', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('membership_status_codes', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('membership_status_codes', sa.Column('updated_date', sa.DateTime(), nullable=True))
    op.add_column('membership_status_codes', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('membership_status_codes', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.add_column('met_users', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('met_users', sa.Column('updated_by', sa.String(length=50), nullable=True))
    op.alter_column('met_users', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('submission', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('survey', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('widget', 'updated_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('widget', 'created_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('widget', 'updated_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('widget_item', 'updated_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('widget_item', 'created_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('widget_item', 'updated_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.add_column('widget_type', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('widget_type', sa.Column('updated_date', sa.DateTime(), nullable=True))
    op.add_column('widget_type', sa.Column('created_by', sa.String(length=50), nullable=True))
    op.add_column('widget_type', sa.Column('updated_by', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('widget_type', 'updated_by')
    op.drop_column('widget_type', 'created_by')
    op.drop_column('widget_type', 'updated_date')
    op.drop_column('widget_type', 'created_date')
    op.alter_column('widget_item', 'updated_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('widget_item', 'created_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('widget_item', 'updated_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('widget', 'updated_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('widget', 'created_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('widget', 'updated_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('survey', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('submission', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('met_users', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('met_users', 'updated_by')
    op.drop_column('met_users', 'created_by')
    op.drop_column('membership_status_codes', 'updated_by')
    op.drop_column('membership_status_codes', 'created_by')
    op.drop_column('membership_status_codes', 'updated_date')
    op.drop_column('membership_status_codes', 'created_date')
    op.alter_column('feedback', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('feedback', 'updated_by')
    op.drop_column('feedback', 'created_by')
    op.drop_column('feedback', 'updated_date')
    op.alter_column('engagement_status', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('engagement_status', 'updated_by')
    op.drop_column('engagement_status', 'created_by')
    op.alter_column('email_verification', 'type',
               existing_type=postgresql.ENUM('Survey', 'RejectedComment', 'Subscribe', name='emailverificationtype'),
               nullable=True)
    op.alter_column('email_verification', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('contact', 'updated_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('contact', 'created_by',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('contact', 'updated_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('comment_status', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('comment_status', 'updated_by')
    op.drop_column('comment_status', 'created_by')
    op.alter_column('comment', 'created_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###
