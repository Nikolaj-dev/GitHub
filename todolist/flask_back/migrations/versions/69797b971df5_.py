"""empty message

Revision ID: 69797b971df5
Revises: 
Create Date: 2023-02-09 20:56:23.220322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69797b971df5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_flask',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_flask')
    # ### end Alembic commands ###
