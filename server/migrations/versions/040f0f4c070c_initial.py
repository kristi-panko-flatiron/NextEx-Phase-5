"""initial"


Revision ID: 040f0f4c070c
Revises: 
Create Date: 2023-10-26 16:48:51.590765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040f0f4c070c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('astrological_signs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sign_name', sa.String(length=20), nullable=False),
    sa.Column('sign_description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('match_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('best_matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('astrological_sign_id', sa.Integer(), nullable=True),
    sa.Column('best_match_name', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['astrological_sign_id'], ['astrological_signs.id'], name=op.f('fk_best_matches_astrological_sign_id_astrological_signs')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.String(length=50), nullable=False),
    sa.Column('astrological_sign_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['astrological_sign_id'], ['astrological_signs.id'], name=op.f('fk_users_astrological_sign_id_astrological_signs')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_matches',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['match_id'], ['matches.id'], name=op.f('fk_user_matches_match_id_matches')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_matches_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'match_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_matches')
    op.drop_table('users')
    op.drop_table('best_matches')
    op.drop_table('matches')
    op.drop_table('astrological_signs')
    # ### end Alembic commands ###
