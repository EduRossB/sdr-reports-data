"""empty message

Revision ID: b07cd73dd7fa
Revises: 8a398b86f4bd
Create Date: 2024-04-17 17:27:11.922967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b07cd73dd7fa'
down_revision = '8a398b86f4bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lista1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('email_address', sa.String(length=80), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('position', sa.String(length=100), nullable=False),
    sa.Column('connected_on', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lista2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('linkedin_url', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('seniority', sa.String(length=100), nullable=True),
    sa.Column('last_contacted', sa.Date(), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('industry', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lista2')
    op.drop_table('lista1')
    # ### end Alembic commands ###
