class SessionsController < ApplicationController
  skip_before_action :ensure_login, only: [:new, :create]

  def new
  end

  def create
    @user = User.find_by(username: params[:user][:username])
    @pwd = params[:user][:password]
    if @user && @user.authenticate(@pwd)
      session[:user_id] = @user.id
      redirect_to root_path, notice: 'Logged in successfully"'
    else
      redirect_to login_path, alert: 'Login failed.'
    end
  end

  def destroy
    reset_session
    redirect_to login_path, alert: 'You have been logged out'
  end
end
