"""initial migration

Revision ID: 5197cde1cd4a
Revises: 
Create Date: 2024-10-03 05:56:19.774109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5197cde1cd4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('hire_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('onboardings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orientation', sa.DateTime(), nullable=True),
    sa.Column('forms_complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('summary', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('onboardings')
    op.drop_table('employees')
    # ### end Alembic commands ###
