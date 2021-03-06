"""empty message

Revision ID: 345bc63cd37a
Revises:
Create Date: 2021-07-01 15:30:52.440679

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '345bc63cd37a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jigasya_members',
                    sa.Column('telegram_id', sa.Integer(), autoincrement=False,
                              nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('telegram_id')
                    )
    op.create_index(op.f('ix_jigasya_members_telegram_id'), 'jigasya_members',
                    ['telegram_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_jigasya_members_telegram_id'),
                  table_name='jigasya_members')
    op.drop_table('jigasya_members')
    # ### end Alembic commands ###
