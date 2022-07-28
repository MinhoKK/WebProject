"""empty message

Revision ID: 70712cd3e48e
Revises: 72d803b9079f
Create Date: 2022-05-28 23:53:09.170232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70712cd3e48e'
down_revision = '72d803b9079f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('signup__data', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_signup__data_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_signup__data_user_id'), ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('signup__data', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_signup__data_user_id'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_signup__data_email'), type_='unique')

    # ### end Alembic commands ###