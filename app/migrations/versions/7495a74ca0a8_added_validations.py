"""added validations

Revision ID: 7495a74ca0a8
Revises: 5185c0d09bca
Create Date: 2024-04-17 20:37:25.545807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7495a74ca0a8'
down_revision = '5185c0d09bca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leave',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('leaveType', sa.String(), nullable=False),
    sa.Column('startDate', sa.DateTime(), nullable=False),
    sa.Column('endDate', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Leave')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Leave',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('leaveType', sa.VARCHAR(), nullable=False),
    sa.Column('startDate', sa.DATETIME(), nullable=False),
    sa.Column('endDate', sa.DATETIME(), nullable=False),
    sa.Column('status', sa.VARCHAR(), nullable=False),
    sa.Column('employee_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('leave')
    # ### end Alembic commands ###
