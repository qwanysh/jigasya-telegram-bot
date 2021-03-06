"""empty message

Revision ID: fd50ff8ad8e2
Revises: 345bc63cd37a
Create Date: 2021-07-01 16:37:34.016210

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'fd50ff8ad8e2'
down_revision = '345bc63cd37a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('jigasya_members', 'username',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('jigasya_members', 'username',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    # ### end Alembic commands ###
